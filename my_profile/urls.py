from . import views
from django.urls import path


urlpatterns = [
    path('<str:username>/', views.profile, name='profile'),
]