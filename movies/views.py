from django.shortcuts import render, redirect
from .models import Movie
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from .forms import UserForm, Creation_form
from django.contrib.auth.decorators import login_required


def base(request):
    al_movies = Movie.objects.all()
    context = {'al_movies': al_movies}
    return render(request, 'movies/index.html', context)


@login_required(login_url='login')
def home_page(request):
    user_query = str(request.GET.get('query', ''))
    search_result = Movie.objects.filter(name__icontains=user_query)
    context = {'search_result': search_result}
    if request.method == 'POST':
        form = Creation_form(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('home_page')
    else:
        form = Creation_form()
        context = {'form': form, 'search_result': search_result}
    return render(request, 'movies/movies_stuff.html', context)


@login_required(login_url='login')
def edit(request, pk):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes')
        }
        try:
            movie_obj = Movie.objects.get(id=pk)
            movie_obj.name = data.get('name')
            movie_obj.picture = data.get('picture')
            movie_obj.rating = data.get('rating')
            movie_obj.notes = data.get('notes')
            movie_obj.save()
            messages.success(request, f"Movie updated - {data.get('name')}")
        except Exception as e:
            messages.warning(
                request, 'Got an error when trying to update movie: {}'.format(e))
        return redirect('home_page')


@login_required(login_url='login')
def delete(request, movie_id):
    try:
        movie_obj = Movie.objects.get(id=movie_id)
        movie_name = movie_obj.name
        movie_obj.delete()
        messages.warning(request, f'Deleted movie: {movie_name}')
    except Exception as e:
        messages.warning(request, f'Got an error when trying to delete a movie: {e}')
    return redirect('home_page')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, f'account is created by user {user}')
                return redirect('login')
        else:
            form = UserForm()
            context = {'form': form}
            return render(request, 'movies/register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.warning(request, 'invalid username or password')

        return render(request, 'movies/login.html', )


@login_required(login_url='login')
def logout_url(request):
    logout(request)
    return redirect('/')
