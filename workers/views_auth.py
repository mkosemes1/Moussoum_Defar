from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Worker
from .serializers import (
    WorkerRegisterSerializer, WorkerLoginSerializer,
    WorkerSerializer, WorkerUpdateSerializer
)


class WorkerRegisterView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        serializer = WorkerRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        worker = serializer.save()

        refresh = RefreshToken.for_user(worker.user)

        return Response({
            'user': {
                'id': worker.user.id,
                'username': worker.user.username,
                'email': worker.user.email,
            },
            'worker': WorkerSerializer(worker).data,
            'tokens': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        }, status=status.HTTP_201_CREATED)


class WorkerLoginView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        serializer = WorkerLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if user is None:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            worker = Worker.objects.get(user=user)
        except Worker.DoesNotExist:
            return Response(
                {'error': 'Worker profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'worker': WorkerSerializer(worker).data,
            'tokens': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        })


class WorkerProfileView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        try:
            worker = Worker.objects.get(user=request.user)
        except Worker.DoesNotExist:
            return Response(
                {'error': 'Worker profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(WorkerSerializer(worker).data)

    def update(self, request):
        try:
            worker = Worker.objects.get(user=request.user)
        except Worker.DoesNotExist:
            return Response(
                {'error': 'Worker profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = WorkerUpdateSerializer(worker, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(WorkerSerializer(worker).data)
