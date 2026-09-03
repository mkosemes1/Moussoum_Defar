from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg, Count
from .models import (
    Language, Country, Worker, WorkerLevel,
    DataCollection, DataSubmission, QualityLog
)
from .serializers import (
    LanguageSerializer, CountrySerializer, WorkerSerializer,
    WorkerCreateSerializer, WorkerScoreSerializer,
    DataCollectionSerializer, DataSubmissionSerializer,
    QualityLogSerializer
)


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.filter(is_active=True)
    serializer_class = LanguageSerializer
    permission_classes = [permissions.AllowAny]


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.filter(is_active=True)
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]


class WorkerViewSet(viewsets.ModelViewSet):
    serializer_class = WorkerSerializer

    def get_queryset(self):
        return Worker.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return WorkerCreateSerializer
        return WorkerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def me(self, request):
        worker, created = Worker.objects.get_or_create(user=request.user)
        serializer = WorkerSerializer(worker)
        return Response(serializer.data)

    @action(detail=False, methods=['put'])
    def update_profile(self, request):
        worker, created = Worker.objects.get_or_create(user=request.user)
        serializer = WorkerCreateSerializer(worker, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(WorkerSerializer(worker).data)

    @action(detail=False, methods=['get'])
    def score(self, request):
        worker, created = Worker.objects.get_or_create(user=request.user)
        worker.calculate_quality_score()
        serializer = WorkerScoreSerializer(worker)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def tasks(self, request):
        worker, created = Worker.objects.get_or_create(user=request.user)
        submissions = DataSubmission.objects.filter(worker=worker)
        serializer = DataSubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def earnings(self, request):
        worker, created = Worker.objects.get_or_create(user=request.user)
        return Response({
            'balance': str(worker.balance),
            'total_tasks': worker.total_tasks,
            'quality_score': worker.quality_score,
            'level': worker.level,
        })


class DataCollectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataCollection.objects.filter(status='active')
    serializer_class = DataCollectionSerializer

    def get_queryset(self):
        queryset = DataCollection.objects.filter(status='active')
        data_type = self.request.query_params.get('data_type')
        language = self.request.query_params.get('language')
        country = self.request.query_params.get('country')

        if data_type:
            queryset = queryset.filter(data_type=data_type)
        if language:
            queryset = queryset.filter(language__code=language)
        if country:
            queryset = queryset.filter(country__code=country)

        return queryset

    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        collection = self.get_object()
        worker, created = Worker.objects.get_or_create(user=request.user)

        serializer = DataSubmissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(worker=worker, collection=collection)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DataSubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = DataSubmissionSerializer

    def get_queryset(self):
        return DataSubmission.objects.filter(worker__user=self.request.user)

    def perform_create(self, serializer):
        worker, created = Worker.objects.get_or_create(user=self.request.user)
        serializer.save(worker=worker)
