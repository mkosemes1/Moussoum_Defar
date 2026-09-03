"""
Worker scoring system.
"""
from django.db.models import Avg, Count
from .models import Worker, QualityLog, DataSubmission


class WorkerScoringSystem:
    """Advanced scoring system for workers."""

    # Weights for quality score calculation
    WEIGHTS = {
        'accuracy': 0.4,
        'volume': 0.3,
        'consistency': 0.2,
        'recency': 0.1,
    }

    # Level thresholds
    LEVEL_THRESHOLDS = {
        1: {'tasks': 0, 'accuracy': 0},
        2: {'tasks': 100, 'accuracy': 80},
        3: {'tasks': 500, 'accuracy': 85},
        4: {'tasks': 1000, 'accuracy': 90},
        5: {'tasks': 5000, 'accuracy': 95},
    }

    @classmethod
    def calculate_quality_score(cls, worker):
        """
        Calculate composite quality score for a worker.
        
        Score = (accuracy * 0.4) + (volume * 0.3) + (consistency * 0.2) + (recency * 0.1)
        """
        # Accuracy score (0-40)
        accuracy_score = worker.accuracy * cls.WEIGHTS['accuracy']

        # Volume score (0-30)
        volume_score = min(worker.total_tasks / 1000, 1.0) * 30 * cls.WEIGHTS['volume']

        # Consistency score (0-20)
        consistency_score = cls._calculate_consistency(worker) * 20 * cls.WEIGHTS['consistency']

        # Recency score (0-10)
        recency_score = cls._calculate_recency(worker) * 10 * cls.WEIGHTS['recency']

        total_score = accuracy_score + volume_score + consistency_score + recency_score

        return round(total_score, 2)

    @classmethod
    def _calculate_consistency(cls, worker):
        """
        Measure quality consistency over time.
        Returns a score between 0 and 1.
        """
        recent_logs = QualityLog.objects.filter(
            worker=worker
        ).order_by('-created_at')[:50]

        if len(recent_logs) < 10:
            return 0.5

        scores = [log.score for log in recent_logs]
        mean = sum(scores) / len(scores)
        if mean == 0:
            return 0.5

        variance = sum((s - mean) ** 2 for s in scores) / len(scores)
        std_dev = variance ** 0.5

        # Lower standard deviation means higher consistency
        return max(0, 1.0 - (std_dev / mean))

    @classmethod
    def _calculate_recency(cls, worker):
        """
        Measure recent worker activity.
        Returns a score between 0 and 1.
        """
        from django.utils import timezone
        from datetime import timedelta

        recent_submissions = DataSubmission.objects.filter(
            worker=worker,
            status='approved'
        ).order_by('-submitted_at')[:10]

        if not recent_submissions:
            return 0

        # Check if worker submitted data in the last 7 days
        last_submission = recent_submissions[0].submitted_at
        days_since = (timezone.now() - last_submission).days

        if days_since <= 7:
            return 1.0
        elif days_since <= 30:
            return 0.7
        elif days_since <= 90:
            return 0.4
        else:
            return 0.1

    @classmethod
    def determine_level(cls, worker):
        """
        Determine worker level based on performance.
        """
        current_level = worker.level

        # Check each level from top to bottom
        for level in range(5, 0, -1):
            thresholds = cls.LEVEL_THRESHOLDS[level]
            if (
                worker.total_tasks >= thresholds['tasks'] and
                worker.accuracy >= thresholds['accuracy']
            ):
                return level

        return 1

    @classmethod
    def update_worker_score(cls, worker):
        """
        Update worker score and level.
        """
        worker.quality_score = cls.calculate_quality_score(worker)
        worker.level = cls.determine_level(worker)
        worker.save(update_fields=['quality_score', 'level'])
        return worker

    @classmethod
    def get_worker_stats(cls, worker):
        """
        Return comprehensive worker statistics.
        """
        from django.utils import timezone
        from datetime import timedelta

        # Basic statistics
        total_submissions = DataSubmission.objects.filter(worker=worker).count()
        approved_submissions = DataSubmission.objects.filter(
            worker=worker, status='approved'
        ).count()
        rejected_submissions = DataSubmission.objects.filter(
            worker=worker, status='rejected'
        ).count()

        # Average quality score
        avg_quality = QualityLog.objects.filter(
            worker=worker
        ).aggregate(avg=Avg('score'))['avg'] or 0

        # Recent activity (last 7 days)
        week_ago = timezone.now() - timedelta(days=7)
        recent_tasks = DataSubmission.objects.filter(
            worker=worker,
            submitted_at__gte=week_ago
        ).count()

        # Top skills
        top_languages = worker.languages.all()[:5]

        return {
            'quality_score': worker.quality_score,
            'level': worker.level,
            'level_display': worker.get_level_display(),
            'total_tasks': worker.total_tasks,
            'accuracy': worker.accuracy,
            'total_submissions': total_submissions,
            'approved_submissions': approved_submissions,
            'rejected_submissions': rejected_submissions,
            'avg_quality': round(avg_quality, 2),
            'recent_tasks': recent_tasks,
            'top_languages': [lang.name for lang in top_languages],
            'can_advance': cls._can_advance_level(worker),
        }

    @classmethod
    def _can_advance_level(cls, worker):
        """
        Check if worker can advance to the next level.
        """
        next_level = worker.level + 1
        if next_level > 5:
            return False

        thresholds = cls.LEVEL_THRESHOLDS[next_level]
        return (
            worker.total_tasks >= thresholds['tasks'] and
            worker.accuracy >= thresholds['accuracy']
        )
