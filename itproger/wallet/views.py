from django.shortcuts import render, redirect
from .forms import UserRegistration, UserAuthorization
from django.contrib.auth import authenticate, login, logout


def account(request):
    if request.user.is_authenticated:
        return redirect('/about')
    if request.method == 'POST':
        if 'password2' in request.POST:
            user_form = UserRegistration(request.POST)
            if user_form.is_valid():
                user_form.save()
                user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
                login(request, user)
        else:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
        return redirect('/about')

    user_form_1 = UserRegistration()
    user_form_2 = UserAuthorization()
    return render(request, 'wallet/profile.html', {'user_form_1': user_form_1, 'user_form_2': user_form_2})


def signout(request):
    logout(request)
    return redirect('/')


def about(request):
    return render(request, 'wallet/about.html', {'title': 'Про нас'})


def calendar(request):
    return render(request, 'wallet/about.html', {'title': 'Календарь'})


def goals(request):
    return render(request, 'wallet/about.html', {'title': 'Цели'})
