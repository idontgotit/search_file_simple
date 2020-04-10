from django.urls import path
from look_up_file import views

urlpatterns = [
    path('', views.look_file, name='look_file'),
    path('search-file/', views.search_file, name='look_file'),
]
