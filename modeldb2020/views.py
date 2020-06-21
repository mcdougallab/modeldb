from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from . import settings
from . import models

ModelDB = models.ModelDB()


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


def modellist(request):
    object_id = request.GET.get('id')
    print('modellist')
    if object_id is None:
        return listbymodelname(request)
    '''
    obj = ModelDB.object_by_id(object_id)
    print(obj)
    if obj is None:
        return listbymodelname(request)
    context = {
        'title': 'ModelDB: Models that contain {}'.format(obj.name),
        'obj': obj
    }
    return render(request, 'modeldb/modellist.html', context)
    '''
    return HttpResponse("Not implemented")

def listbymodelname(request):
    context = {
        'title': 'ModelDB: Models List',
        'all_models': ModelDB.models_by_name()
    }
    return render(request, 'listbymodelname.html', context)

    

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
