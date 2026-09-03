from celery import shared_task
from django.utils import timezone
import requests
import time
import json
from .models import Evaluation, TestCase, TestExecution, AfricanBenchmark
from .scoring import score_response


@shared_task(bind=True)
def evaluate_model(self, evaluation_id):
    """Evaluate an AI model against an African benchmark."""
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
    language_scores = {}

    for test_case in test_cases:
        try:
            start_time = time.time()

            # Get model response
            model_response = get_model_response(evaluation, test_case)

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

            # Track language scores
            lang = evaluation.benchmark.language_code
            if lang not in language_scores:
                language_scores[lang] = []
            language_scores[lang].append(score)

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
    evaluation.score_by_language = {
        lang: sum(scores) / len(scores)
        for lang, scores in language_scores.items()
    }
    evaluation.status = 'completed'
    evaluation.completed_at = timezone.now()
    evaluation.save()


def get_model_response(evaluation, test_case):
    """
    Get response from the client's model.
    
    Supports multiple methods:
    1. Direct API call (model_endpoint provided)
    2. Simulated response (for testing)
    """
    if not evaluation.model_endpoint:
        # Simulate response for testing
        return f"Simulated response for: {test_case.input_text[:50]}..."

    # Build the request payload
    payload = build_request_payload(test_case, evaluation)
    headers = build_request_headers(evaluation)

    try:
        response = requests.post(
            evaluation.model_endpoint,
            json=payload,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()
        return extract_response_content(response.json())
    except requests.exceptions.RequestException as e:
        raise Exception(f"Model API error: {str(e)}")


def build_request_payload(test_case, evaluation):
    """
    Build the request payload for the model API.
    
    Standard format:
    {
        "input": "question text",
        "context": "optional context",
        "language": "fr",
        "benchmark": "senegal"
    }
    """
    return {
        'input': test_case.input_text,
        'context': test_case.context,
        'language': evaluation.benchmark.language_code,
        'benchmark': evaluation.benchmark.country_code,
        'category': test_case.category,
        'difficulty': test_case.difficulty,
    }


def build_request_headers(evaluation):
    """Build request headers including API key."""
    headers = {
        'Content-Type': 'application/json',
    }
    if evaluation.model_api_key:
        headers['Authorization'] = f'Bearer {evaluation.model_api_key}'
    return headers


def extract_response_content(response_data):
    """
    Extract the model's response content from various response formats.
    
    Supported formats:
    - {"output": "response"}  (standard)
    - {"response": "response"} (alternative)
    - {"answer": "response"}  (alternative)
    - {"result": "response"}  (alternative)
    - {"message": "response"} (alternative)
    - {"text": "response"}    (alternative)
    - {"content": "response"} (alternative)
    """
    possible_keys = ['output', 'response', 'answer', 'result', 'message', 'text', 'content']
    
    for key in possible_keys:
        if key in response_data:
            return response_data[key]
    
    # If no known key found, try to use the response directly if it's a string
    if isinstance(response_data, str):
        return response_data
    
    raise Exception(f"Could not extract response from: {json.dumps(response_data)[:200]}...")
