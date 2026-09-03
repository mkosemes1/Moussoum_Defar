from django.urls import path
from .views import RegisterView, LoginView

urlpatterns_auth = [
    path('register/', RegisterView.as_view({'post': 'create'}), name='auth-register'),
    path('login/', LoginView.as_view({'post': 'create'}), name='auth-login'),
]
