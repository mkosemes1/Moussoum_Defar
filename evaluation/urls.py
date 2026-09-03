from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AfricanBenchmarkViewSet, EvaluationViewSet, APIKeyViewSet
)

router = DefaultRouter()
router.register(r'benchmarks', AfricanBenchmarkViewSet)
router.register(r'evaluations', EvaluationViewSet, basename='evaluation')
router.register(r'api-keys', APIKeyViewSet, basename='apikey')

urlpatterns = [
    path('', include(router.urls)),
]
