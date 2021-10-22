"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from blog import views


urlpatterns = [
    path("blog/", include("blog.urls", namespace="blog")),
    path("", include("core.urls", namespace="core")),
    url(r"^api/blog/$", views.BlogViewSet.as_view(), name="blog"),
    url(r"^api/category/$", views.CategoryViewSet.as_view(), name="category"),
    path("admin/", admin.site.urls),
]
