from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Language(models.Model):
    """African languages supported by the platform."""
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.code})"


class Country(models.Model):
    """African countries."""
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=10, default='FCFA')
    mobile_money_services = models.JSONField(default=list)
    languages = models.ManyToManyField(Language, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'countries'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.code})"


class Worker(models.Model):
    """African worker profile."""
    LEVEL_CHOICES = [
        (1, 'Data Worker'),
        (2, 'Verified Annotator'),
        (3, 'Language Specialist'),
        (4, 'AI Evaluator'),
        (5, 'Domain Expert'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='worker_profile')
    phone = models.CharField(max_length=20, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=1)
    quality_score = models.FloatField(default=0.0)
    total_tasks = models.IntegerField(default=0)
    accuracy = models.FloatField(default=0.0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_verified = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-quality_score']

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - Level {self.level}"

    def calculate_quality_score(self):
        """Calculate quality score based on accuracy and volume."""
        accuracy_score = self.accuracy * 40
        volume_score = min(self.total_tasks / 1000, 1.0) * 30
        consistency_score = self._calculate_consistency() * 30
        self.quality_score = accuracy_score + volume_score + consistency_score
        self.save(update_fields=['quality_score'])
        return self.quality_score

    def _calculate_consistency(self):
        """Measure quality consistency over time."""
        recent_logs = QualityLog.objects.filter(
            worker=self
        ).order_by('-created_at')[:50]

        if len(recent_logs) < 10:
            return 0.5

        scores = [log.score for log in recent_logs]
        mean = sum(scores) / len(scores)
        if mean == 0:
            return 0.5

        variance = sum((s - mean) ** 2 for s in scores) / len(scores)
        std_dev = variance ** 0.5

        return max(0, 1.0 - (std_dev / mean))


class WorkerLevel(models.Model):
    """Level and progression requirements."""
    LEVEL_CHOICES = [
        (1, 'Data Worker'),
        (2, 'Verified Annotator'),
        (3, 'Language Specialist'),
        (4, 'AI Evaluator'),
        (5, 'Domain Expert'),
    ]

    worker = models.OneToOneField(Worker, on_delete=models.CASCADE, related_name='level_info')
    level = models.IntegerField(choices=LEVEL_CHOICES)
    tasks_required = models.IntegerField(default=100)
    accuracy_required = models.FloatField(default=80.0)
    unlocked_at = models.DateTimeField(null=True, blank=True)
    tasks_at_unlock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.worker} - Level {self.level}"

    def can_advance(self):
        """Check if the worker can advance to the next level."""
        return (
            self.worker.total_tasks >= self.tasks_required and
            self.worker.accuracy >= self.accuracy_required
        )


class DataCollection(models.Model):
    """Data collection project."""
    DATA_TYPE_CHOICES = [
        ('audio', 'Audio'),
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('document', 'Document'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    data_type = models.CharField(max_length=10, choices=DATA_TYPE_CHOICES)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    target_count = models.IntegerField(default=1000)
    current_count = models.IntegerField(default=0)
    price_per_item = models.DecimalField(max_digits=8, decimal_places=4)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    instructions = models.TextField(blank=True)
    sample_data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'data collections'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.get_data_type_display()})"

    @property
    def progress_percentage(self):
        if self.target_count == 0:
            return 0
        return (self.current_count / self.target_count) * 100

    @property
    def is_complete(self):
        return self.current_count >= self.target_count


class DataSubmission(models.Model):
    """Worker data submission."""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('review', 'Under Review'),
    ]

    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='submissions')
    collection = models.ForeignKey(DataCollection, on_delete=models.CASCADE, related_name='submissions')
    file = models.FileField(upload_to='submissions/%Y/%m/%d/')
    transcription = models.TextField(blank=True)
    metadata = models.JSONField(default=dict)
    quality_score = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    reviewer_notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.worker} - {self.collection.title} - {self.status}"

    def approve(self, score=1.0):
        """Approve the submission."""
        self.status = 'approved'
        self.quality_score = score
        self.save()
        self.collection.current_count += 1
        self.collection.save(update_fields=['current_count'])
        self.worker.total_tasks += 1
        self.worker.accuracy = (
            (self.worker.accuracy * (self.worker.total_tasks - 1) + score * 100)
            / self.worker.total_tasks
        )
        self.worker.save(update_fields=['total_tasks', 'accuracy'])
        QualityLog.objects.create(worker=self.worker, submission=self, score=score)

    def reject(self, reason=''):
        """Reject the submission."""
        self.status = 'rejected'
        self.reviewer_notes = reason
        self.save()


class QualityLog(models.Model):
    """Submission quality history."""
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='quality_logs')
    submission = models.ForeignKey(DataSubmission, on_delete=models.CASCADE)
    score = models.FloatField()
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.worker} - Score: {self.score}"
