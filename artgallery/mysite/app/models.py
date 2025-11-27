from django.db import models


# *** ВИДАЛЕНО: Клас Artist видалено, оскільки дані керуються через Contentful ***
    
class Gallery(models.Model):
    # Залишаємо лише базові поля
    name_ua = models.CharField(max_length=200, verbose_name="Назва (UA)")
    name_en = models.CharField(max_length=200, verbose_name="Name (EN)")

    # ВИДАЛЕНО поля: city_ua, city_en, description_ua, description_en, url
    
    image = models.ImageField(upload_to='gallery/', verbose_name="Зображення")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # ВИДАЛЕНО: зв'язок ManyToMany з Artist
    
    def __str__(self):
        return self.name_ua or self.name_en

    class Meta:
        db_table = 'public_gallery'
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
