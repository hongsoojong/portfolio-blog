from django.shortcuts import render


def main(request):
    return render(request, "main.html")


def all_posts(request):
    return render(request, "blog.html")


def post1(request):
    return render(request, "posts/post1.html")


def post2(request):
    return render(request, "posts/post2.html")


def post3(request):
    return render(request, "posts/post3.html")


def post4(request):
    return render(request, "posts/post4.html")

def post5(request):
    return render(request, "posts/post5.html")