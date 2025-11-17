from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Gallery
from .serializers import GallerySerializer

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all().order_by('-created_at')
    serializer_class = GallerySerializer
    
    # Пошук за назвою (name_ua + name_en)
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter
    ]
    search_fields = ['name_ua', 'name_en']           # Task 4.1
    filterset_fields = ['city_ua', 'city_en']        # Task 4.2
    ordering_fields = ['created_at', 'name_ua']