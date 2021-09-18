from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = "categories"


class Blog(models.Model):

    title = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
    contents = models.TextField(blank=True)
    pub_date = models.DateField(blank=True)
