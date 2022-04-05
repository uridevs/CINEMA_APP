from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Films, Director, Genre
from .forms import FilmForm, DirectorForm
from django.db.models import Q
# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    films = Films.objects.filter(
        Q(genre__name__icontains=q) | 
        Q(name__icontains=q) |
        Q(sinopsis__icontains=q) |
        Q(author__name__icontains=q)
        ) # When filtering films, it will show only the values that match "q" or whatever if value is != None, otherwise it will show all

    genres = Genre.objects.all()
    directors = Director.objects.all()
    film_count = films.count()

    context = {'films': films, 'genres': genres, 'film_count': film_count, 'directors': directors}
    return render(request, 'catalogoapp/home.html', context)

def film(request, pk):
    film = Films.objects.get(id=pk)
    context = {'film': film}
    return render(request, 'catalogoapp/film.html', context)

def create_film(request):
    form = FilmForm()

    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'catalogoapp/film_form.html', context)

def update_film(request, pk):
    film = Films.objects.get(id=pk)
    form = FilmForm(instance=film)

    if request.method == 'POST':
        form = FilmForm(request.POST, instance=film) #instead of creating a new room, its gonna change the values on the specified room
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/film_form.html', context)

def director(request, pk):
    director = Director.objects.get(id=pk)
    context = {'director': director}
    return render(request, 'catalogoapp/director.html', context)



def create_director(request):
    form = DirectorForm()

    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'catalogoapp/director_form.html', context)

def delete_film(request, pk):
    film = Films.objects.get(id=pk)
    
    if request.method == 'POST':
        film.delete()
        return redirect('home')
        
    return render(request, 'base/delete.html', {'obj':film})