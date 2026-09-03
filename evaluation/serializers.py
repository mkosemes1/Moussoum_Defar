from rest_framework import serializers
from .models import (
    AfricanBenchmark, TestCase, Evaluation, TestExecution, APIKey
)


class AfricanBenchmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AfricanBenchmark
        fields = [
            'id', 'name', 'description', 'country_code', 'country_name',
            'version', 'language_code', 'language_name', 'category',
            'test_count', 'is_active', 'created_at', 'updated_at'
        ]


class TestCaseSerializer(serializers.ModelSerializer):
    benchmark_name = serializers.CharField(source='benchmark.name', read_only=True)

    class Meta:
        model = TestCase
        fields = [
            'id', 'benchmark', 'benchmark_name', 'input_text',
            'expected_output', 'context', 'category', 'difficulty',
            'scoring_criteria', 'tags', 'is_active'
        ]


class TestExecutionSerializer(serializers.ModelSerializer):
    test_case = TestCaseSerializer(read_only=True)

    class Meta:
        model = TestExecution
        fields = [
            'id', 'evaluation', 'test_case', 'model_response',
            'score', 'scoring_details', 'latency_ms', 'executed_at'
        ]


class EvaluationSerializer(serializers.ModelSerializer):
    benchmark = AfricanBenchmarkSerializer(read_only=True)
    benchmark_id = serializers.IntegerField(write_only=True)
    success_rate = serializers.ReadOnlyField()

    class Meta:
        model = Evaluation
        fields = [
            'id', 'client', 'benchmark', 'benchmark_id', 'model_name',
            'model_endpoint', 'status', 'results', 'score_overall',
            'score_by_category', 'score_by_language', 'total_tests',
            'passed_tests', 'failed_tests', 'avg_latency_ms',
            'success_rate', 'created_at', 'completed_at'
        ]
        read_only_fields = [
            'client', 'status', 'results', 'score_overall',
            'score_by_category', 'score_by_language', 'total_tests',
            'passed_tests', 'failed_tests', 'avg_latency_ms',
            'completed_at'
        ]


class EvaluationCreateSerializer(serializers.Serializer):
    benchmark_id = serializers.IntegerField()
    model_name = serializers.CharField(max_length=200)
    model_endpoint = serializers.URLField(required=False, allow_blank=True)
    model_api_key = serializers.CharField(max_length=200, required=False, allow_blank=True)


class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = ['id', 'name', 'key', 'is_active', 'rate_limit', 'created_at', 'last_used_at']
        read_only_fields = ['key', 'created_at', 'last_used_at']
