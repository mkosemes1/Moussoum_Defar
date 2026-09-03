from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LanguageViewSet, CountryViewSet, WorkerViewSet,
    DataCollectionViewSet, DataSubmissionViewSet
)

router = DefaultRouter()
router.register(r'languages', LanguageViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'profile', WorkerViewSet, basename='worker')
router.register(r'collections', DataCollectionViewSet)
router.register(r'submissions', DataSubmissionViewSet, basename='submission')

urlpatterns = [
    path('', include(router.urls)),
]
