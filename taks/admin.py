from django.contrib import admin
from .models import downloader, User
# Register your models here.


class DownloadAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("id", "name", "topic", "text")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("topic",)
    # добавляем возможность фильтрации по дате
    list_filter = ("id",)
    empty_value_display = "-пусто-"


class UserAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("id", "name", "username", "email", "address", "phone", "website", "company")


admin.site.register(downloader, DownloadAdmin)
admin.site.register(User, UserAdmin)
