from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("category/c/post/1", views.post1, name="post1"),
    path("category/c/post/2", views.post2, name="post2"),
    path("category/c/post/3", views.post3, name="post3"),
    path("category/basic/post/4", views.post4, name="post4"),
    path("category/c/post/5", views.post5, name="post5"),
    path("category/basic/", views.cate_basic, name="cate-basic"),
    path("category/c/", views.cate_c, name="cate-c"),
    path("category/algorithm//", views.cate_algorithm, name="cate-algorithm"),
    path("", views.all_posts, name="all-posts"),
]
