from django.shortcuts import render


def main(request):
    return render(request, "main.html")


def all_posts(request):
    return render(request, "blog/main_blog.html")


def cate_basic(request):
    return render(request, "blog/post_categories/cate_basic.html")


def cate_c(request):
    return render(request, "blog/post_categories/cate_c.html")


def cate_algorithm(request):
    return render(request, "blog/post_categories/cate_algorithm.html")


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
