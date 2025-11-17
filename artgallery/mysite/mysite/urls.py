from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from app.views import GalleryViewSet

router = DefaultRouter()
router.register(r'galleries', GalleryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    
    path('api/auth/', include('dj_rest_auth.urls')),# АУТЕНТИФІКАЦІЯ
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)