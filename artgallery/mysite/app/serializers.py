from rest_framework import serializers
from .models import Gallery, Artist   # ← ДОДАЙ Artist тут!


# Серіалізатор для художників
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio']


# Серіалізатор для галерей
class GallerySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    artists = ArtistSerializer(many=True, read_only=True)  # ← вкладені художники

    class Meta:
        model = Gallery
        fields = [
            'id', 'name_ua', 'name_en',
            'city_ua', 'city_en',
            'description_ua', 'description_en',
            'image', 'url',
            'artists',                    # ← тепер є!
            'created_at', 'updated_at'
        ]