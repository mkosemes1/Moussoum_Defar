from django.urls import path
from .views_auth import WorkerRegisterView, WorkerLoginView, WorkerProfileView

urlpatterns = [
    path('register/', WorkerRegisterView.as_view({'post': 'create'}), name='worker-register'),
    path('login/', WorkerLoginView.as_view({'post': 'create'}), name='worker-login'),
    path('profile/', WorkerProfileView.as_view({'get': 'list', 'put': 'update'}), name='worker-profile'),
]
