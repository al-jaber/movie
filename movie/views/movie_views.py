from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from movie.models import Movie
from movie.forms import MovieForm


@login_required
def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    context = {'movie': movie}

    if request.method == 'GET':
        return render(request, 'blog/movie_confirm_delete.html', context)
    elif request.method == 'POST':
        movie.delete()
        messages.success(request,  'The movie has been deleted successfully.')
        return redirect('movies')


@login_required
def update_movie(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.method == 'GET':
        context = {'form': MovieForm(instance=movie), 'id': id}
        return render(request, 'blog/movie_form.html', context)

    elif request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The movie has been updated successfully.')
            return redirect('movies')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/movie_form.html', {'form': form})


@login_required
def create_movie(request):
    if request.method == 'GET':
        context = {'form': MovieForm()}
        return render(request, 'blog/movie_form.html', context)
    elif request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The movie has been created successfully.')
            return redirect('movies')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/movie_form.html', {'form': form})


def movie_list(request):
    # Retrieve all movies or filter by search query
    query = request.GET.get('search')
    if query:
        movies = Movie.objects.filter(name__icontains=query)
    else:
        movies = Movie.objects.all()

    return render(request, 'home.html', {'movies': movies})

def home(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'home.html', context)
