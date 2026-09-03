from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, ClientViewSet

router = DefaultRouter()
router.register(r'register', RegisterView, basename='register')
router.register(r'login', LoginView, basename='login')
router.register(r'profile', ClientViewSet, basename='client')

urlpatterns_auth = [
    path('register/', RegisterView.as_view({'post': 'create'}), name='auth-register'),
    path('login/', LoginView.as_view({'post': 'create'}), name='auth-login'),
]

urlpatterns = [
    path('', include(router.urls)),
]
