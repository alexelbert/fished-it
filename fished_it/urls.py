from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("my_profile/", include("my_profile.urls")),
    path("", include("catches.urls")),
    path("accounts/", include("allauth.urls")),
]
