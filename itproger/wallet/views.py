from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegistration, UserAuthorization
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, date, timedelta
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .utils import Calendar
import calendar


def account(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST':
        if 'password2' in request.POST:
            user_form_1 = UserRegistration(request.POST)
            if user_form_1.is_valid():
                user = user_form_1.save()
                prof = Profile()
                prof.user = user
                Profile.objects.create(user=prof.user, money=0)
                user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return redirect('/home')
        else:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('/home')
    user_form_1 = UserRegistration()
    user_form_2 = UserAuthorization()
    return render(request, 'wallet/profile.html', {'user_form_1': user_form_1, 'user_form_2': user_form_2})


def signout(request):
    logout(request)
    return redirect('/')


def about(request):
    return render(request, 'wallet/about.html', {'title': 'Про нас'})


class CalendarView(generic.ListView):
    model = Event
    template_name = 'wallet/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def goals(request):
    return render(request, 'wallet/about.html', {'title': 'Цели'})


def main(request):
    return render(request, 'wallet/index.html', {'title': 'Главная'})