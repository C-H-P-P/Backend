from rest_framework import viewsets, filters
# ВИДАЛЕНО: from django_filters.rest_framework import DjangoFilterBackend
from .models import Gallery
from .serializers import GallerySerializer

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all().order_by('-created_at')
    serializer_class = GallerySerializer
    
    # ВИДАЛЕНО: filter_backends = [...] та search_fields = [...] 
    # Залишаємо лише OrderingFilter
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'name_ua']
