from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.core import serializers

from accounts.forms import UserForm, LoginForm


# Create your views here.
def register(request: HttpRequest):
    """ Registers a user """
    if request.method == 'POST':
        form = UserForm(data=request.POST)

        if not form.is_valid():
            return redirect('/accounts/register')

        user = form.save()
        request.session['user'] = serializers.serialize('json', [user])
        return redirect(f'/accounts/{user.id}')

    return render(request, 'register.html', context={'form': UserForm()})


def login(request: HttpRequest):
    """ Logs a user in"""
    if request.method == 'POST':
        pass

    return render(request, 'login.html', context={'form': LoginForm()})


def profile(request: HttpRequest, profile_id):
    """ Opens the profile of a user """
    return render(request, 'base.html')

