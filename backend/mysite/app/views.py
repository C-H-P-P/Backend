from rest_framework import viewsets, filters
from .models import Gallery
from .serializers import GallerySerializer

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all().order_by('-created_at')
    serializer_class = GallerySerializer
    
  
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'name_ua']
