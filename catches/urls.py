from . import views
from django.urls import path

urlpatterns = [
    path('', views.CatchesList.as_view(), name='home'),
    path('<slug:slug>/', views.catch_detail, name='catch_detail'),
]