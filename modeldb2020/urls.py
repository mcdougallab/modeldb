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
from django.urls import path, re_path, include
from . import views, urls_api_v1

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?:modeldb/)?index.html$(?i)', views.index, name='index'),
    re_path('^(?:modeldb/)?login$(?i)', views.my_login, name='login'),
    re_path('^(?:modeldb/)?logout$(?i)', views.my_logout, name='logout'),
    re_path(r'^(?:modeldb/)?search(?:fulltext)?(?:\.(?:cs)?html)?$(?i)', views.search, name='search'),
    re_path(r'^(?:modeldb/)?neuron_dwnldguide(?:\.(?:cs)?html)?$(?i)', views.static, {'page': 'neuron_download_guide', 'title': 'NEURON download help'}, name='neuron_download_guide'),
    re_path(r'^(?:modeldb/)?howtocite(?:\.(?:cs)?html)?$(?i)', views.static, {'page': 'howtocite', 'title': 'How to cite ModelDB'}, name='howtocite'),
    re_path(r'^(?:modeldb/)?api(?:\.(?:cs)?html)?$(?i)', views.static, dict(page='apidocs', title='The ModelDB API'), name='apidocs'),
    re_path(r'^(?:modeldb/)?(?:mdb)?resources(?:\.(?:cs)?html)?$(?i)', views.static, dict(page='mdbresources', title='Web resources for ModelDB'), name='mdbresources'),
    re_path(r'^(?:modeldb/)?eco(?:\.(?:cs)?html)?$(?i)', views.static, dict(page='eco', title='An ecosystem of computational neuroscience resources'), name='eco'),
    re_path(r'^(?:modeldb/)?listbymodelname(?:\.(?:cs)?html)?$(?i)', views.listbymodelname, name='listbymodelname'),
    re_path(r'^(?:modeldb/)?modellist(?:\.(?:cs)?html)?$(?i)', views.modellist, name='modellist'),
    re_path(r'^(?:modeldb/)?help(?:menu)?(?:\.(?:cs)?html)?$(?i)', views.static, dict(page='help', title='Help'), name='help'),
    re_path(r'^(?:modeldb/)?showmodel(?:\.(?:cs)?html)?(?:\.asp)?$(?i)', views.showmodel, name='showmodel'),
    re_path(r'^(?:modeldb/)?eavbindown(?:\.(?:cs)?html)?$(?i)', views.download_zip, name='download_zip'),    
    re_path(r'^(?:modeldb/)?getmodelfile(?:\.(?:cs)?html)?$(?i)', views.download, name='download_file'),
    re_path(r'^(?:modeldb/)?findbycurrent(?:\.(?:cs)?html)?$(?i)', views.findbycurrent, name='findbycurrent'),
    re_path(r'^(?:modeldb/)?findbyregionlist(?:\.(?:cs)?html)?$(?i)', views.findbyregionlist, name='findbyregion'), 
    re_path(r'^(?:modeldb/)?findbyregiontable(?:\.(?:cs)?html)?$(?i)', views.findbyregionlist, name='findbyregion'), # not clear that we want to keep table as a separate thing
    re_path(r'^(?:modeldb/)?findbyreceptor(?:\.(?:cs)?html)?$(?i)', views.findbyreceptor, name='findbyreceptor'),
    re_path(r'^(?:modeldb/)?findbytransmitter(?:\.(?:cs)?html)?$(?i)', views.findbytransmitter, name='findbytransmitter'),
    re_path(r'^(?:modeldb/)?findbygenelist(?:\.(?:cs)?html)?$(?i)', views.findbygene, name='findbygene'),
    re_path(r'^(?:modeldb/)?findbyconcept(?:\.(?:cs)?html)?$(?i)', views.findbyconcept, name='findbyconcept'),
    re_path(r'^(?:modeldb/)?findbysimulator(?:\.(?:cs)?html)?$(?i)', views.findbysimulator, name='findbysimulator'),
    re_path(r'^(?:modeldb/)?(?:mdb)?citations(?:\.(?:cs)?html)?$(?i)', views.mdbcitations, name='mdbcitations'),
    #path('admin/', admin.site.urls),
    re_path(r'^api/v1/', include(urls_api_v1)),
    path('<slug:model_id>', views.showmodel_redirect, name='showmodel_redirect')
]
