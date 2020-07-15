
from django.contrib import admin
from django.urls import path, re_path, include
from . import api_v1

urlpatterns = [
    path('', api_v1.index),
    path('models/<int:model_id>', api_v1.models_view),
    path('models/<slug:field>', api_v1.models_view),
    path('models', api_v1.models_view),
    path('celltypes/<int:_id>', api_v1.celltypes_view),
    path('celltypes/<slug:field>', api_v1.celltypes_view),
    path('celltypes', api_v1.celltypes_view),
    path('currents/<int:_id>', api_v1.currents_view),
    path('currents/<slug:field>', api_v1.currents_view),
    path('currents', api_v1.currents_view),
    path('genes/<int:_id>', api_v1.genes_view),
    path('genes/<slug:field>', api_v1.genes_view),
    path('genes', api_v1.genes_view),
    path('regions/<int:_id>', api_v1.regions_view),
    path('regions/<slug:field>', api_v1.regions_view),
    path('regions', api_v1.regions_view),
    path('receptors/<int:_id>', api_v1.receptors_view),
    path('receptors/<slug:field>', api_v1.receptors_view),
    path('receptors', api_v1.receptors_view),
    path('transmitters/<int:_id>', api_v1.transmitters_view),
    path('transmitters/<slug:field>', api_v1.transmitters_view),
    path('transmitters', api_v1.transmitters_view),
    path('simenvironments/<int:_id>', api_v1.simenvironments_view),
    path('simenvironments/<slug:field>', api_v1.simenvironments_view),
    path('simenvironments', api_v1.simenvironments_view),
    path('modelconcepts/<int:_id>', api_v1.modelconcepts_view),
    path('modelconcepts/<slug:field>', api_v1.modelconcepts_view),
    path('modelconcepts', api_v1.modelconcepts_view),
    path('modeltypes/<int:_id>', api_v1.modeltypes_view),
    path('modeltypes/<slug:field>', api_v1.modeltypes_view),
    path('modeltypes', api_v1.modeltypes_view),
    path('papers/<int:_id>', api_v1.papers_view),
    path('papers/<slug:field>', api_v1.papers_view),
    path('papers', api_v1.papers_view),
    path('morphology/<int:_id>', api_v1.morphology_view)
]
