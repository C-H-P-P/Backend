from django.contrib import admin
from .models import Gallery
from django.contrib.auth.models import User

# *** ВИДАЛЕНО: Artist (якщо він тут був, то видаляємо) ***

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    # list_display, search_fields тепер відображають лише спрощену модель Gallery
    list_display = ('name_ua', 'name_en', 'created_at')
    search_fields = ('name_ua', 'name_en')
    readonly_fields = ('created_at', 'updated_at')

# *** ДОДАНО: Реєстрація User для відображення юзерів, створених через /api/auth/registration/ (Task 5.3) ***
# Хоча User вже може бути зареєстрований за замовчуванням, явна реєстрація 
# або налаштування відображення є гарною практикою.
# Якщо ви не використовуєте кастомний User, цей рядок можна залишити.
# admin.site.register(User) 
# (Якщо User вже відображається, не змінюйте. Якщо ні — додайте це, або краще налаштуйте його відображення.)
