from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = ("title", "category", "contents", "pub_date")

    pass
