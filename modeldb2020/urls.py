"""modeldb2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^index.html$(?i)', views.index, name='index'),
    re_path('^login$(?i)', views.my_login, name='login'),
    re_path('^logout$(?i)', views.my_logout, name='logout'),
    re_path(r'^neuron_dwnldguide(?:\.(?:cs)?html)?$(?i)', views.static, {'page': 'neuron_download_guide', 'title': 'NEURON download help'}, name='neuron_download_guide'),
    re_path(r'^howtocite(?:\.(?:cs)?html)?$(?i)', views.static, {'page': 'howtocite', 'title': 'How to cite ModelDB'}, name='howtocite'),
    re_path(r'^mdbresources(?:\.(?:cs)?html)?$(?i)', views.static, dict(page='mdbresources', title='Web resources for ModelDB'), name='mdbresources'),
    re_path(r'^eco(?:\.(?:cs)?html)?$(?i)', views.static, dict(page='eco', title='An ecosystem of computational neuroscience resources'), name='eco'),
    re_path(r'^(?:modeldb/)?help(?:menu)?(?:\.(?:cs)?html)?$(?i)', views.static, dict(page='help', title='Help'), name='help'),
    path('admin/', admin.site.urls),
]
