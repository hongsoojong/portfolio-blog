from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("post/1", views.post1, name="post1"),
    path("post/2", views.post2, name="post2"),
    path("post/3", views.post3, name="post3"),
    path("post/4", views.post4, name="post4"),
    path("post/5", views.post5, name="post5"),
    path("post/6", views.post6, name="post6"),
    path("post/7", views.post7, name="post7"),
    path("post/8", views.post8, name="post8"),
    path("post/9", views.post9, name="post9"),
    path("post/10", views.post10, name="post10"),
    path("post/11", views.post11, name="post11"),
    path("post/12", views.post12, name="post12"),
    path("post/13", views.post13, name="post13"),
    path("post/14", views.post14, name="post14"),
    path("post/15", views.post15, name="post15"),
    path("post/16", views.post16, name="post16"),
    path("post/<int:blog_pk>", views.detail, name="detail"),
    path("", views.all_posts, name="all-posts"),
]
