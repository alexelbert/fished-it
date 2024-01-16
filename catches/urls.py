from . import views
from django.urls import path

urlpatterns = [
     path('', views.CatchesList.as_view(), name='home'),
     path('add_catch/', views.add_catch, name='add_catch'),
     path('<slug:slug>/', views.catch_detail, name='catch_detail'),
     path('<slug:slug>/edit_comment/<int:comment_id>',
          views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_comment/<int:comment_id>',
          views.comment_delete, name='comment_delete'),
]