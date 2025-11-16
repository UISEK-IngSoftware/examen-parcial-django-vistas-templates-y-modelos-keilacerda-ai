from django.shortcuts import render

def index(request):
    peliculas = ['Película 1', 'Película 2', 'Película 3', 'Película 4']
    return render(request, 'index.html', {
        'peliculas': peliculas
    })

def pelicula_details(request, pelicula):
    return render(request, 'pelicula_details.html', {
        'pelicula' : pelicula
    } )