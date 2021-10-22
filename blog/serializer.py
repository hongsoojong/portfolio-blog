from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = ("name", "count")

    def get_count(self, obj):
        return models.Blog.objects.filter(category__name=obj.name).count()


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = models.Blog
        fields = "__all__"
