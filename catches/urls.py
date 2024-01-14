from . import views
from django.urls import path

urlpatterns = [
    path('', views.CatchesList.as_view(), name='home'),
]