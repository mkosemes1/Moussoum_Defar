"""
Système de scoring pour les workers.
"""
from django.db.models import Avg, Count
from .models import Worker, QualityLog, DataSubmission


class WorkerScoringSystem:
    """Système de scoring avancé pour les workers."""

    # Poids pour le calcul du score qualité
    WEIGHTS = {
        'accuracy': 0.4,
        'volume': 0.3,
        'consistency': 0.2,
        'recency': 0.1,
    }

    # Seuils pour les niveaux
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
        Calcule le score qualité composite d'un worker.
        
        Score = (accuracy * 0.4) + (volume * 0.3) + (consistency * 0.2) + (recency * 0.1)
        """
        # Score d'accuracy (0-40)
        accuracy_score = worker.accuracy * cls.WEIGHTS['accuracy']

        # Score de volume (0-30)
        volume_score = min(worker.total_tasks / 1000, 1.0) * 30 * cls.WEIGHTS['volume']

        # Score de constance (0-20)
        consistency_score = cls._calculate_consistency(worker) * 20 * cls.WEIGHTS['consistency']

        # Score de récence (0-10)
        recency_score = cls._calculate_recency(worker) * 10 * cls.WEIGHTS['recency']

        total_score = accuracy_score + volume_score + consistency_score + recency_score

        return round(total_score, 2)

    @classmethod
    def _calculate_consistency(cls, worker):
        """
        Mesure la constance de la qualité dans le temps.
        Retourne un score entre 0 et 1.
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

        # Plus l'écart-type est faible, plus la constance est élevée
        return max(0, 1.0 - (std_dev / mean))

    @classmethod
    def _calculate_recency(cls, worker):
        """
        Mesure l'activité récente du worker.
        Retourne un score entre 0 et 1.
        """
        from django.utils import timezone
        from datetime import timedelta

        recent_submissions = DataSubmission.objects.filter(
            worker=worker,
            status='approved'
        ).order_by('-submitted_at')[:10]

        if not recent_submissions:
            return 0

        # Vérifier si le worker a soumis des données dans les 7 derniers jours
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
        Détermine le niveau d'un worker basé sur ses performances.
        """
        current_level = worker.level

        # Vérifier chaque niveau de haut en bas
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
        Met à jour le score et le niveau d'un worker.
        """
        worker.quality_score = cls.calculate_quality_score(worker)
        worker.level = cls.determine_level(worker)
        worker.save(update_fields=['quality_score', 'level'])
        return worker

    @classmethod
    def get_worker_stats(cls, worker):
        """
        Retourne les statistiques complètes d'un worker.
        """
        from django.utils import timezone
        from datetime import timedelta

        # Statistiques de base
        total_submissions = DataSubmission.objects.filter(worker=worker).count()
        approved_submissions = DataSubmission.objects.filter(
            worker=worker, status='approved'
        ).count()
        rejected_submissions = DataSubmission.objects.filter(
            worker=worker, status='rejected'
        ).count()

        # Score moyen
        avg_quality = QualityLog.objects.filter(
            worker=worker
        ).aggregate(avg=Avg('score'))['avg'] or 0

        # Activité récente (7 derniers jours)
        week_ago = timezone.now() - timedelta(days=7)
        recent_tasks = DataSubmission.objects.filter(
            worker=worker,
            submitted_at__gte=week_ago
        ).count()

        # Top compétences
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
        Vérifie si le worker peut passer au niveau supérieur.
        """
        next_level = worker.level + 1
        if next_level > 5:
            return False

        thresholds = cls.LEVEL_THRESHOLDS[next_level]
        return (
            worker.total_tasks >= thresholds['tasks'] and
            worker.accuracy >= thresholds['accuracy']
        )
