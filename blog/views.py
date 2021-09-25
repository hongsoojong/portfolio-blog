from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from . import models


def detail(request, blog_pk):
    blog_detail = get_object_or_404(models.Blog, pk=blog_pk)
    return render(request, "blog/detail_blog.html", {"blog_detail": blog_detail})


def all_posts(request):
    blogs = models.Blog.objects
    categories = models.Category.objects
    post_list = models.Blog.objects.all().order_by("-pk")
    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(
        request,
        "blog/main_blog.html",
        {"blogs": blogs, "posts": posts, "categories": categories},
    )


def post1(request):
    return render(request, "blog/all_posts/post1.html")


def post2(request):
    return render(request, "blog/all_posts/post2.html")


def post3(request):
    return render(request, "blog/all_posts/post3.html")


def post4(request):
    return render(request, "blog/all_posts/post4.html")


def post5(request):
    return render(request, "blog/all_posts/post5.html")


def post6(request):
    return render(request, "blog/all_posts/post6.html")


def post7(request):
    return render(request, "blog/all_posts/post7.html")


def post8(request):
    return render(request, "blog/all_posts/post8.html")


def post9(request):
    return render(request, "blog/all_posts/post9.html")


def post10(request):
    return render(request, "blog/all_posts/post10.html")
