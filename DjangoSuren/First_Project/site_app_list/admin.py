from django.contrib import admin

# Register your models here.

from site_app_list.models import Example1

@admin.register(Example1)
class ExampleAdmin(admin.ModelAdmin):

    list_display = "id", "title", "description", "aga" #делаем красивое отображение страницы "Example1"/ "title", "done" берем с models.py
    list_display_links = "id", "title" #типа ссылку теперь имеет не только id но и title