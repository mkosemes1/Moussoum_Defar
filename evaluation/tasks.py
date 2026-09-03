from celery import shared_task
from django.utils import timezone
import requests
import time
from .models import Evaluation, TestCase, TestExecution
from .scoring import score_response


@shared_task(bind=True)
def evaluate_model(self, evaluation_id):
    """Évalue un modèle IA contre un benchmark africain."""
    try:
        evaluation = Evaluation.objects.get(id=evaluation_id)
    except Evaluation.DoesNotExist:
        return

    evaluation.status = 'running'
    evaluation.save()

    test_cases = TestCase.objects.filter(
        benchmark=evaluation.benchmark,
        is_active=True
    )

    total_tests = test_cases.count()
    evaluation.total_tests = total_tests
    evaluation.save()

    passed = 0
    failed = 0
    total_latency = 0
    category_scores = {}

    for test_case in test_cases:
        try:
            start_time = time.time()

            if evaluation.model_endpoint:
                # Call the model API
                response = requests.post(
                    evaluation.model_endpoint,
                    json={'input': test_case.input_text},
                    headers={'Authorization': f'Bearer {evaluation.model_api_key}'},
                    timeout=30
                )
                model_response = response.json().get('output', '')
            else:
                # Simulate model response for testing
                model_response = f"Simulated response for: {test_case.input_text[:50]}..."

            latency_ms = int((time.time() - start_time) * 1000)

            # Score the response
            score, details = score_response(test_case, model_response)

            TestExecution.objects.create(
                evaluation=evaluation,
                test_case=test_case,
                model_response=model_response,
                score=score,
                scoring_details=details,
                latency_ms=latency_ms
            )

            total_latency += latency_ms

            if score >= 70:
                passed += 1
            else:
                failed += 1

            # Track category scores
            cat = test_case.category or 'uncategorized'
            if cat not in category_scores:
                category_scores[cat] = []
            category_scores[cat].append(score)

        except Exception as e:
            # Log error and continue
            failed += 1
            TestExecution.objects.create(
                evaluation=evaluation,
                test_case=test_case,
                model_response=f"Error: {str(e)}",
                score=0,
                scoring_details={'error': str(e)},
                latency_ms=0
            )

    # Update evaluation results
    evaluation.passed_tests = passed
    evaluation.failed_tests = failed
    evaluation.avg_latency_ms = total_latency / total_tests if total_tests > 0 else 0
    evaluation.score_overall = sum(
        cat_score for scores in category_scores.values()
        for cat_score in scores
    ) / total_tests if total_tests > 0 else 0
    evaluation.score_by_category = {
        cat: sum(scores) / len(scores)
        for cat, scores in category_scores.items()
    }
    evaluation.status = 'completed'
    evaluation.completed_at = timezone.now()
    evaluation.save()
