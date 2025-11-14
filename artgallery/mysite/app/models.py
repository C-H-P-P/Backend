from django.db import models

class Gallery(models.Model):
    name_ua = models.CharField(max_length=200, verbose_name="Назва (UA)")
    name_en = models.CharField(max_length=200, verbose_name="Name (EN)")
    description_ua = models.TextField(blank=True, verbose_name="Опис (UA)")
    description_en = models.TextField(blank=True, verbose_name="Description (EN)")
    image = models.ImageField(upload_to='gallery/', verbose_name="Зображення")
    url = models.URLField(blank=True, null=True, verbose_name="Посилання")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_ua or self.name_en

    class Meta:
        db_table = 'public_gallery'
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
