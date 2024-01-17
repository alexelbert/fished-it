from . import views
from django.urls import path

urlpatterns = [
     path('', views.CatchesList.as_view(), name='home'),
     path('add_catch/', views.add_catch, name='add_catch'),
     path('my_catches/', views.my_catches, name='my_catches'),
     path('edit_catch/<slug:slug>/', views.edit_catch, name='edit_catch'),
     path('delete_catch/<slug:slug>/', views.delete_catch, name='delete_catch'),
     path('<slug:slug>/', views.catch_detail, name='catch_detail'),
     path('<slug:slug>/edit_comment/<int:comment_id>',
          views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_comment/<int:comment_id>',
          views.comment_delete, name='comment_delete'),
]