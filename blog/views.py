from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from . import models
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.serializer import BlogSerializer, CategorySerializer


class BlogViewSet(APIView):
    def get(self, request, format=None):
        queryset = models.Blog.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(APIView):
    def get(self, request, format=None):
        queryset = models.Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


# 프로그래밍 기초 카테고리
def category_basic(request):
    categories = models.Category.objects
    post_list = models.Blog.objects.filter(category_id="1").order_by("-pk")
    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(
        request,
        "blog/main_blog.html",
        {
            "question_list": posts,
            "posts": posts,
            "categories": categories,
        },
    )


# C언어 카테고리
def category_c(request):
    categories = models.Category.objects
    post_list = models.Blog.objects.filter(category_id="2").order_by("-pk")
    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(
        request,
        "blog/main_blog.html",
        {
            "question_list": posts,
            "posts": posts,
            "categories": categories,
        },
    )


# 알고리즘 카테고리
def category_algorithm(request):
    categories = models.Category.objects
    post_list = models.Blog.objects.filter(category_id="3").order_by("-pk")
    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(
        request,
        "blog/main_blog.html",
        {
            "question_list": posts,
            "posts": posts,
            "categories": categories,
        },
    )


# 게임수학 카테고리
def category_math(request):
    categories = models.Category.objects
    post_list = models.Blog.objects.filter(category_id="4").order_by("-pk")
    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(
        request,
        "blog/main_blog.html",
        {
            "question_list": posts,
            "posts": posts,
            "categories": categories,
        },
    )


# 실습과 그림으로 배우는 리눅스 구조 카테고리
def category_os(request):
    categories = models.Category.objects
    post_list = models.Blog.objects.filter(category_id="5").order_by("-pk")
    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(
        request,
        "blog/main_blog.html",
        {
            "question_list": posts,
            "posts": posts,
            "categories": categories,
        },
    )


def detail(request, blog_pk):
    blog_detail = get_object_or_404(models.Blog, pk=blog_pk)
    return render(request, "blog/detail_blog.html", {"blog_detail": blog_detail})


def all_posts(request):
    blogs = models.Blog.objects
    categories = models.Category.objects
    page = request.GET.get("page", "1")
    post_list = models.Blog.objects.all().order_by("-pk")
    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    return render(
        request,
        "blog/main_blog.html",
        {
            "question_list": posts,
            "blogs": blogs,
            "posts": posts,
            "categories": categories,
        },
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


def post11(request):
    return render(request, "blog/all_posts/post11.html")


def post12(request):
    return render(request, "blog/all_posts/post12.html")


def post13(request):
    return render(request, "blog/all_posts/post13.html")


def post14(request):
    return render(request, "blog/all_posts/post14.html")


def post15(request):
    return render(request, "blog/all_posts/post15.html")


def post16(request):
    return render(request, "blog/all_posts/post16.html")


def post17(request):
    return render(request, "blog/all_posts/post17.html")


def post18(request):
    return render(request, "blog/all_posts/post18.html")


def post19(request):
    return render(request, "blog/all_posts/post19.html")


def post20(request):
    return render(request, "blog/all_posts/post20.html")


def post21(request):
    return render(request, "blog/all_posts/post21.html")


def post22(request):
    return render(request, "blog/all_posts/post22.html")


def post23(request):
    return render(request, "blog/all_posts/post23.html")


def post24(request):
    return render(request, "blog/all_posts/post24.html")


def post25(request):
    return render(request, "blog/all_posts/post25.html")


def post26(request):
    return render(request, "blog/all_posts/post26.html")


def post27(request):
    return render(request, "blog/all_posts/post27.html")


def post28(request):
    return render(request, "blog/all_posts/post28.html")


def post29(request):
    return render(request, "blog/all_posts/post29.html")


def post30(request):
    return render(request, "blog/all_posts/post30.html")


def post31(request):
    return render(request, "blog/all_posts/post31.html")


def post32(request):
    return render(request, "blog/all_posts/post32.html")


def post33(request):
    return render(request, "blog/all_posts/post33.html")
