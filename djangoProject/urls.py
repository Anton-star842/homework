from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path("", lambda request: redirect("login")),
    path("admin/", admin.site.urls),
    path("register/", include("myapp.urls")),
    path("login/", include("myapp.urls")),
    path("courses/", include("myapp.urls")),
    path("", include("myapp.urls")),
]
