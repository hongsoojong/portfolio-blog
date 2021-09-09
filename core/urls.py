from django.urls import path
from blog import views as blog_views


app_name = "core"

urlpatterns = [path("", blog_views.main, name="home")]
