from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Client auth
    path('api/v1/auth/', include('clients.urls_auth')),
    # Worker auth
    path('api/v1/workers/auth/', include('workers.urls_auth')),
    # API endpoints
    path('api/v1/workers/', include('workers.urls')),
    path('api/v1/', include('evaluation.urls')),
    path('api/v1/clients/', include('clients.urls')),
    # Web pages
    re_path(r'^templates/(?P<path>.*)$', serve, {'document_root': settings.BASE_DIR / 'templates'}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
