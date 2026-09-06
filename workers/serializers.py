from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import (
    Language, Country, Worker, WorkerLevel,
    DataCollection, DataSubmission, QualityLog
)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'code', 'name', 'region', 'is_active']


class CountrySerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'code', 'name', 'currency', 'mobile_money_services', 'languages']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class WorkerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    country = CountrySerializer(read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    level_display = serializers.CharField(source='get_level_display', read_only=True)

    class Meta:
        model = Worker
        fields = [
            'id', 'user', 'phone', 'country', 'languages',
            'level', 'level_display', 'quality_score', 'total_tasks',
            'accuracy', 'balance', 'is_verified', 'bio',
            'created_at', 'updated_at'
        ]


class WorkerRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)
    phone = serializers.CharField(max_length=20, required=False, default='')
    country = serializers.CharField(max_length=10, required=False, allow_blank=True, allow_null=True)
    languages = serializers.ListField(
        child=serializers.CharField(max_length=10), required=False, default=[]
    )
    bio = serializers.CharField(required=False, default='', allow_blank=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return attrs

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        phone = validated_data.get('phone', '')
        country_code = validated_data.get('country', '')
        lang_codes = validated_data.get('languages', [])
        bio = validated_data.get('bio', '')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        country = None
        if country_code:
            country = Country.objects.filter(code=country_code).first()

        worker = Worker.objects.create(
            user=user,
            phone=phone,
            country=country,
            bio=bio
        )

        if lang_codes:
            langs = Language.objects.filter(code__in=lang_codes)
            worker.languages.set(langs)

        return worker


class WorkerLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class WorkerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['phone', 'country', 'languages', 'bio']


class WorkerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['phone', 'country', 'languages', 'bio']


class WorkerScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['quality_score', 'total_tasks', 'accuracy', 'level']


class DataCollectionSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only=True)
    country = CountrySerializer(read_only=True)
    progress_percentage = serializers.ReadOnlyField()
    is_complete = serializers.ReadOnlyField()

    class Meta:
        model = DataCollection
        fields = [
            'id', 'title', 'description', 'data_type', 'language', 'country',
            'target_count', 'current_count', 'price_per_item', 'status',
            'instructions', 'progress_percentage', 'is_complete',
            'created_at', 'updated_at'
        ]


class DataSubmissionSerializer(serializers.ModelSerializer):
    worker = WorkerSerializer(read_only=True)
    collection = DataCollectionSerializer(read_only=True)
    collection_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = DataSubmission
        fields = [
            'id', 'worker', 'collection', 'collection_id', 'file',
            'transcription', 'metadata', 'quality_score', 'status',
            'reviewer_notes', 'submitted_at', 'reviewed_at'
        ]
        read_only_fields = ['worker', 'quality_score', 'status', 'reviewer_notes', 'reviewed_at']


class QualityLogSerializer(serializers.ModelSerializer):
    worker = WorkerSerializer(read_only=True)

    class Meta:
        model = QualityLog
        fields = ['id', 'worker', 'submission', 'score', 'reviewer', 'notes', 'created_at']
