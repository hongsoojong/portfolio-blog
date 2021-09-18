from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Blog


def home(request):
    post_list = Blog.objects.all().order_by("-pk")
    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(request, "home.html", {"posts": posts})
