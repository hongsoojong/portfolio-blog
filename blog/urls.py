from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("post/1", views.post1, name="post1"),
    path("post/2", views.post2, name="post2"),
    path("post/3", views.post3, name="post3"),
    path("post/4", views.post4, name="post4"),
    path("post/5", views.post5, name="post5"),
    path("", views.all_posts, name="all-posts"),
]
