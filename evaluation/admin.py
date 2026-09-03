from django.contrib import admin
from .models import AfricanBenchmark, TestCase, Evaluation, TestExecution, APIKey


@admin.register(AfricanBenchmark)
class AfricanBenchmarkAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'country_code', 'country_name', 'version',
        'language_name', 'category', 'test_count', 'is_active'
    ]
    list_filter = ['country_code', 'category', 'is_active']
    search_fields = ['name', 'country_name', 'description']


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = [
        'benchmark', 'input_text', 'difficulty', 'category', 'is_active'
    ]
    list_filter = ['benchmark', 'difficulty', 'category', 'is_active']
    search_fields = ['input_text', 'expected_output']


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = [
        'client', 'model_name', 'benchmark', 'status',
        'score_overall', 'total_tests', 'passed_tests', 'created_at'
    ]
    list_filter = ['status', 'benchmark']
    search_fields = ['model_name', 'client__username']
    readonly_fields = [
        'score_overall', 'score_by_category', 'score_by_language',
        'total_tests', 'passed_tests', 'failed_tests', 'avg_latency_ms'
    ]


@admin.register(TestExecution)
class TestExecutionAdmin(admin.ModelAdmin):
    list_display = ['evaluation', 'test_case', 'score', 'latency_ms', 'executed_at']
    list_filter = ['executed_at']
    search_fields = ['evaluation__model_name']
    readonly_fields = ['model_response', 'scoring_details']


@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'is_active', 'rate_limit', 'created_at', 'last_used_at']
    list_filter = ['is_active']
    search_fields = ['name', 'user__username']
    readonly_fields = ['key', 'last_used_at']
