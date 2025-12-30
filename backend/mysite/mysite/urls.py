from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# Імпортуємо твої в'юшки
from app.views import GalleryViewSet 
from app.auth_views import MinimalLoginView, MinimalRegisterView, UserDetailView  # <--- ДОДАЙ ЦЕ

router = DefaultRouter()
# Увага: перевір, куди стукає фронтенд: /api/gallery/ чи /api/galleries/
# За стандартом краще множина:
router.register(r'galleries', GalleryViewSet) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # --- АВТОРИЗАЦІЯ ---
    # Використовуємо твої кастомні в'юшки
    path('api/auth/login/', MinimalLoginView.as_view(), name='login'),
    
    # Якщо фронтенд шле запит на /api/auth/register/, залиш 'register/'
    # Якщо фронтенд шле на /api/auth/registration/, зміни на 'registration/'
    path('api/auth/register/', MinimalRegisterView.as_view(), name='register'),
    path('api/auth/user/', UserDetailView.as_view(), name='user_detail'),
]

# Додаємо медіа-файли (картинки)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)