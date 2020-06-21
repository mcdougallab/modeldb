from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from . import settings

ModelDB = {
    'num_models': 1600
}

def index(request):
    context = {
        'title': 'ModelDB',
        'ModelDB': ModelDB,
        'request': request
    }
    return render(request, 'index.html', context)

def static(request, page='', title=''):
    context = {
        'title': f'ModelDB: {title}',
        'request': request
    }
    return render(request, f'{page}.html', context)


def my_logout(request):
    logout(request)
    next_url = request.GET.get('next')
    if next_url:
        return redirect(next_url)
    else:
        return redirect('/')

def my_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if password is not None:
        user = authenticate(username=username, password=password)
        next_url = request.POST.get('next')
        print('next_url', next_url)
        if user is not None:
            login(request, user)
            print('authenticated', user)
            return redirect(request.POST.get('next'))
    else:
        next_url = request.GET.get('next')
        print('next_url', next_url)
    context = {
        'next': next_url
    }
    return render(request, 'login.html', context)
