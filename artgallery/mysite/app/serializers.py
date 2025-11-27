from rest_framework import serializers
from .models import Gallery


# *** ВИДАЛЕНО: ArtistSerializer більше не потрібен ***

# Серіалізатор для галерей
class GallerySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, required=False) 
    # ВИДАЛЕНО: artists = ArtistSerializer(...)

    class Meta:
        model = Gallery
        fields = [
            'id', 
            'name_ua', 
            'name_en',
            # ВИДАЛЕНО: city_ua, city_en, description_ua, description_en, url, artists
            'image',
            'created_at', 'updated_at'
        ]
