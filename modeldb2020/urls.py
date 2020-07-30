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
    re_path('^(?:modeldb/)?login$(?i)', views.my_login, name='login'),
    re_path(r'^(?:modeldb/)?processmodelsubmit?(?:\.(?:cs)?html)?$(?i)', views.process_model_submit, name='processmodelsubmit'),
    re_path(r'^(?:modeldb/)?showmodel(?:\.(?:cs)?html)?(?:\.asp)?$(?i)', views.showmodel, name='showmodel'),
    # NOTE: anything that uses POST should appear above here or the redirects may lose POST data
    # these next two lines standardize the URIs: no modeldb/, no .cshtml or .html
    re_path(r'^modeldb/(?P<uri>.+)$(?i)', views.uri_cleanup_redirect, name='uri_cleanup_redirect'),
    re_path(r'^(?P<uri>.+)\.(?:cs)?html$(?i)', views.uri_cleanup_redirect, name='uri_cleanup_redirect'),
    # back to regular paths
    re_path(r'^index$(?i)', views.index, name='index'),
    re_path('^logout$(?i)', views.my_logout, name='logout'),
    re_path(r'^listbyanyauthor$(?i)', views.list_by_any_author, name='listbyanyauthor'),
    #re_path(r'^listbyfirstauthor$(?i)', views.list_by_first_author, name='listbyfirstauthor'),
    re_path(r'^submitmodel$(?i)', views.submit_model, name='submitmodel'),
    re_path(r'^search$(?i)', views.search, name='search'),
    re_path(r'^searchfulltext$(?i)', views.search_redirect, name='search'),
    re_path(r'^neuron_dwnldguide$(?i)', views.static, {'page': 'neuron_download_guide', 'title': 'NEURON download help'}, name='neuron_download_guide'),
    re_path(r'^howtocite$(?i)', views.static, {'page': 'howtocite', 'title': 'How to cite ModelDB'}, name='howtocite'),
    re_path(r'^trends?$(?i)', views.trends, name='trends'),
    re_path(r'^api$(?i)', views.static, dict(page='apidocs', title='The ModelDB API'), name='apidocs'),
    re_path(r'^(?:mdb)?resources$(?i)', views.static, dict(page='mdbresources', title='Web resources for ModelDB'), name='mdbresources'),
    re_path(r'^guide_neuron_upload$(?i)', views.static, dict(page='guide_neuron_upload', title='Help for preparing a NEURON simulator archive'), name='guide_neuron_upload'),
    re_path(r'^eco$(?i)', views.static, dict(page='eco', title='An ecosystem of computational neuroscience resources'), name='eco'),
    re_path(r'^listbymodelname$(?i)', views.listbymodelname, name='listbymodelname'),
    re_path(r'^modellist$(?i)', views.modellist, name='modellist'),
    re_path(r'^help(?:menu)?$(?i)', views.static, dict(page='help', title='Help'), name='help'),
    re_path(r'^eavbindown$(?i)', views.download_zip, name='download_zip'),    
    re_path(r'^getmodelfile$(?i)', views.download, name='download_file'),
    re_path(r'^findbycurrent$(?i)', views.findbycurrent, name='findbycurrent'),
    re_path(r'^findbyregionlist$(?i)', views.findbyregionlist, name='findbyregion'), 
    re_path(r'^findbyregiontable$(?i)', views.findbyregionlist, name='findbyregion'), # not clear that we want to keep table as a separate thing
    re_path(r'^findbyreceptor$(?i)', views.findbyreceptor, name='findbyreceptor'),
    re_path(r'^findbytransmitter$(?i)', views.findbytransmitter, name='findbytransmitter'),
    re_path(r'^findbygenelist$(?i)', views.findbygene, name='findbygene'),
    re_path(r'^ptrm$(?i)', views.ptrm, name='ptrm'),
    re_path(r'^models-requested-public$(?i)', views.models_requested_public, name='requested_public'),
    re_path(r'^findbyconcept$(?i)', views.findbyconcept, name='findbyconcept'),
    re_path(r'^findbysimulator$(?i)', views.findbysimulator, name='findbysimulator'),
    re_path(r'^(?:mdb)?citations$(?i)', views.mdbcitations, name='mdbcitations'),
    re_path(r'^models-with-uncurated-references$(?i)', views.models_with_uncurated_references, name='uncurated'),
    re_path(r'^forget_access$(?i)', views.forget_access, name='forget_access'),
    re_path(r'^(?P<kind>model)author/(?P<author>.+)$(?i)', views.modelauthor, name='modelauthor'),
    #path('admin/', admin.site.urls),
    re_path(r'^api/v1/', include(urls_api_v1)),
    path('<slug:model_id>', views.showmodel_redirect, name='showmodel_redirect')
]
