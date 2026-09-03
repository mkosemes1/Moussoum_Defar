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
    """
    Serializer for creating a new evaluation.
    
    The client provides:
    - benchmark_id: Which benchmark to test against (e.g., 1 for Senegal)
    - model_name: Name of the model being tested
    - model_endpoint: URL of the model's API (must accept POST with {"input": "..."})
    - model_api_key: API key for authentication (optional)
    
    The model API must:
    - Accept POST requests with JSON body
    - Return JSON with the model's response
    - Support keys: output, response, answer, result, message, text, or content
    """
    benchmark_id = serializers.IntegerField(
        help_text="ID of the benchmark to test against (e.g., 1=Senegal, 2=Nigeria, 3=Kenya)"
    )
    model_name = serializers.CharField(
        max_length=200,
        help_text="Name of your model (e.g., 'My Banking Chatbot')"
    )
    model_endpoint = serializers.URLField(
        required=False,
        allow_blank=True,
        help_text="URL of your model's API endpoint (e.g., https://api.yourmodel.com/predict)"
    )
    model_api_key = serializers.CharField(
        max_length=200,
        required=False,
        allow_blank=True,
        help_text="API key for authentication (optional)"
    )


class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = ['id', 'name', 'key', 'is_active', 'rate_limit', 'created_at', 'last_used_at']
        read_only_fields = ['key', 'created_at', 'last_used_at']
