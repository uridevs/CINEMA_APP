from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('film/<str:pk>', views.film, name="film"),
    path('director/<str:pk>', views.director, name="director"),
    path('create-film/', views.create_film, name="create-film"),
    path('create-director/', views.create_director, name="create-director"),
    path('update-film/<str:pk>/', views.update_film, name="update-film"),
    path('delete-film/<str:pk>/', views.delete_film, name="delete-film"),
]