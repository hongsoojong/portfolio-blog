from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("name",)

    pass


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = ("title", "category", "pub_date")

    pass
