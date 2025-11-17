from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pelicula/<int:identification>/', views.pelicula_details, name='pelicula_details'),
]