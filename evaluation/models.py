from django.db import models
from django.contrib.auth.models import User


class AfricanBenchmark(models.Model):
    """Benchmark by African country/context."""
    CATEGORY_CHOICES = [
        ('cultural', 'Cultural Understanding'),
        ('linguistic', 'Linguistic'),
        ('commercial', 'Commercial'),
        ('administrative', 'Administrative'),
        ('medical', 'Medical'),
        ('agricultural', 'Agricultural'),
        ('financial', 'Financial'),
        ('educational', 'Educational'),
        ('mixed', 'Mixed'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=100)
    version = models.CharField(max_length=10, default='1.0')
    language_code = models.CharField(max_length=10, default='fr')
    language_name = models.CharField(max_length=100, default='French')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='mixed')
    test_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['country_name', 'name']
        unique_together = ['country_code', 'name', 'version']

    def __str__(self):
        return f"{self.name} ({self.country_code} v{self.version})"

    def update_test_count(self):
        self.test_count = self.testcase_set.count()
        self.save(update_fields=['test_count'])


class TestCase(models.Model):
    """African test case."""
    DIFFICULTY_CHOICES = [
        (1, 'Easy'),
        (2, 'Medium'),
        (3, 'Hard'),
        (4, 'Expert'),
        (5, 'Extreme'),
    ]

    benchmark = models.ForeignKey(AfricanBenchmark, on_delete=models.CASCADE)
    input_text = models.TextField()
    expected_output = models.TextField()
    context = models.TextField(help_text="Cultural/commercial/local context")
    category = models.CharField(max_length=50, blank=True)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=2)
    scoring_criteria = models.JSONField(default=dict)
    tags = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['benchmark', 'difficulty']

    def __str__(self):
        return f"[{self.benchmark}] {self.input_text[:50]}..."


class Evaluation(models.Model):
    """AI model evaluation."""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='evaluations')
    benchmark = models.ForeignKey(AfricanBenchmark, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=200)
    model_endpoint = models.URLField(blank=True)
    model_api_key = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    results = models.JSONField(null=True, blank=True)
    score_overall = models.FloatField(null=True, blank=True)
    score_by_category = models.JSONField(default=dict)
    score_by_language = models.JSONField(default=dict)
    total_tests = models.IntegerField(default=0)
    passed_tests = models.IntegerField(default=0)
    failed_tests = models.IntegerField(default=0)
    avg_latency_ms = models.FloatField(default=0)
    error_log = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.model_name} - {self.benchmark.name} - {self.status}"

    @property
    def success_rate(self):
        if self.total_tests == 0:
            return 0
        return (self.passed_tests / self.total_tests) * 100

    def calculate_scores(self):
        """Calculate scores from test executions."""
        executions = self.testexecution_set.all()
        if not executions.exists():
            return

        self.total_tests = executions.count()
        self.passed_tests = executions.filter(score__gte=70).count()
        self.failed_tests = self.total_tests - self.passed_tests
        self.score_overall = executions.aggregate(models.Avg('score'))['score__avg']
        self.avg_latency_ms = executions.aggregate(models.Avg('latency_ms'))['latency_ms__avg']

        # Score by category
        categories = {}
        for execution in executions:
            cat = execution.test_case.category or 'uncategorized'
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(execution.score)

        self.score_by_category = {
            cat: sum(scores) / len(scores)
            for cat, scores in categories.items()
        }

        self.save()


class TestExecution(models.Model):
    """Individual test execution."""
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    model_response = models.TextField()
    score = models.FloatField()
    scoring_details = models.JSONField(default=dict)
    latency_ms = models.IntegerField(default=0)
    executed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-executed_at']

    def __str__(self):
        return f"{self.evaluation} - Test {self.test_case.id} - Score: {self.score}"


class APIKey(models.Model):
    """Client API access key."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_keys')
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=64, unique=True)
    is_active = models.BooleanField(default=True)
    rate_limit = models.IntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.user.username})"
