from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# ПЕРЕВІРКА: Якщо GalleryViewSet знаходиться у mysite/app/views.py, імпорт правильний
from app.views import GalleryViewSet 

router = DefaultRouter()
router.register(r'galleries', GalleryViewSet) # Task 1.7, 1.8

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # /api/galleries/
    
    # Task 3.2: АУТЕНТИФІКАЦІЯ та РЕЄСТРАЦІЯ
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
