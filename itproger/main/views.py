from django.shortcuts import render, redirect
from .forms import UserRegistration, ProfileRegistration, UserAuthorization
from django.contrib.auth import authenticate, login, logout
from main.models import Profile


def signup(request):
    if request.user.is_authenticated:
        return redirect('/about')
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)
        profile_form = ProfileRegistration(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            prof = profile_form.save(commit=False)
            prof.user = user
            prof.save()
            return redirect('/signin')
    else:
        user_form = UserRegistration()
        profile_form = ProfileRegistration()
    return render(request, 'main/profile.html', {'user_form': user_form, 'profile_form': profile_form})
    # return render(request, 'main/index.html', {'title': 'Главная страница'})


def signin(request):
    if request.user.is_authenticated:
        return redirect('/about')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/about')
    user_form = UserAuthorization()
    return render(request, 'main/profile.html', {'user_form': user_form})


def signout(request):
    logout(request)
    return redirect('/signin')


def about(request):
    return render(request, 'main/about.html', {'title': 'Про нас'})


def calendar(request):
    return render(request, 'main/about.html', {'title': 'Календарь'})


def goals(request):
    return render(request, 'main/about.html', {'title': 'Цели'})
