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
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from . import views, urls_api_v1

try:
    from . import pipeline_urls

    pipeline_re_path = [re_path(r"^pipeline/", include(pipeline_urls))]

except ImportError:
    pipeline_re_path = []

urlpatterns = (
    [
        path("", views.index, name="index"),
        path("cookieaccept", views.cookie_accept, name="cookieaccept"),
        path(
            "favicon.ico",
            RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
        ),
        re_path("^login$(?i)", views.my_login, name="login"),
        re_path(
            r"^processmodelsubmit$(?i)",
            views.process_model_submit,
            name="processmodelsubmit",
        ),
        re_path(
            r"^showmodel(?:\.asp)?$(?i)",
            views.showmodel_redirect,
            name="showmodel_redirect",
        ),
        re_path(r"^index$(?i)", views.index, name="index"),
        re_path("^logout$(?i)", views.my_logout, name="logout"),
        re_path(
            r"^listbyanyauthor$(?i)", views.list_by_any_author, name="listbyanyauthor"
        ),
        re_path(
            r"^implementers$(?i)", views.list_by_implementer, name="listbyimplementer"
        ),
        re_path(
            r"implementers/(?P<implementer>.+)", views.implementer, name="implementer"
        ),
        # re_path(r'^listbyfirstauthor$(?i)', views.list_by_first_author, name='listbyfirstauthor'),
        re_path(r"^submitmodel$(?i)", views.submit_model, name="submitmodel"),
        re_path(r"^search$(?i)", views.search, name="search"),
        re_path(r"^searchfulltext$(?i)", views.search_redirect, name="search"),
        re_path(
            r"^neuron_dwnldguide$(?i)",
            views.static,
            {"page": "neuron_download_guide", "title": "NEURON download help"},
            name="neuron_download_guide",
        ),
        re_path(
            r"^privacy-policy$(?i)",
            views.static,
            {"page": "privacy-policy", "title": "Privacy Policy"},
            name="privacy_policy",
        ),
        re_path(
            r"^howtocite$(?i)",
            views.static,
            {"page": "howtocite", "title": "How to cite ModelDB"},
            name="howtocite",
        ),
        re_path(r"^trends?$(?i)", views.trends, name="trends"),
        re_path(
            r"^api$(?i)",
            views.static,
            dict(page="apidocs", title="The ModelDB API"),
            name="apidocs",
        ),
        re_path(
            r"^(?:mdb)?resources$(?i)",
            views.static,
            dict(page="mdbresources", title="Web resources for ModelDB"),
            name="mdbresources",
        ),
        re_path(
            r"^guide_neuron_upload$(?i)",
            views.static,
            dict(
                page="guide_neuron_upload",
                title="Help for preparing a NEURON simulator archive",
            ),
            name="guide_neuron_upload",
        ),
        re_path(
            r"^eco$(?i)",
            views.static,
            dict(
                page="eco", title="An ecosystem of computational neuroscience resources"
            ),
            name="eco",
        ),
        re_path(
            r"^listbymodelname$(?i)", views.listbymodelname, name="listbymodelname"
        ),
        re_path(
            r"^modellist$(?i)", views.modellist_redirect, name="modellist_redirect"
        ),
        re_path(
            r"^modellist/(?P<object_id>[0-9]+)$(?i)", views.modellist, name="modellist"
        ),
        re_path(r"^filelist/(?P<identifier>.+)$(?i)", views.filelist, name="filelist"),
        re_path(
            r"^help(?:menu)?$(?i)",
            views.static,
            dict(page="help", title="Help"),
            name="help",
        ),
        re_path(r"^private-models$(?i)", views.private_models, name="private_models"),
        re_path(r"^top-papers$(?i)", views.top_papers, name="top_papers"),
        re_path(
            r"^eavbindown$(?i)", views.eavdownload_redirect, name="eavdownload_redirect"
        ),
        re_path(
            r"^download/(?P<model_id>[0-9]+)$(?i)",
            views.download_zip,
            name="download_zip",
        ),
        re_path(
            r"^modelview_components/(?P<model_id>[0-9]+)$(?i)",
            views.modelview_components,
            name="modelview_components",
        ),
        re_path(r"^getmodelfile$(?i)", views.download, name="download_file"),
        re_path(r"^getmodelfileexplanation$(?i)", views.get_explanation, name="explain_file"),
        re_path(
            r"^metadata-predictor$(?i)",
            views.metadata_predictor,
            name="metadata_predictor",
        ),
        re_path(r"^findbycurrent$(?i)", views.findbycurrent, name="findbycurrent"),
        re_path(r"^regions$(?i)", views.browse_by_region, name="regions"),
        re_path(r"^findbyregionlist$(?i)", views.findbyregionlist, name="findbyregion"),
        re_path(
            r"^findbyregiontable$(?i)", views.findbyregionlist, name="findbyregion"
        ),  # not clear that we want to keep table as a separate thing
        re_path(r"^findbyreceptor$(?i)", views.findbyreceptor, name="findbyreceptor"),
        re_path(
            r"^findbytransmitter$(?i)",
            views.findbytransmitter,
            name="findbytransmitter",
        ),
        re_path(r"^findbygenelist$(?i)", views.findbygene, name="findbygene"),
        re_path(r"^ptrm$(?i)", views.ptrm, name="ptrm"),
        re_path(
            r"^models-requested-public$(?i)",
            views.models_requested_public,
            name="requested_public",
        ),
        re_path(r"^findbyconcept$(?i)", views.findbyconcept, name="findbyconcept"),
        re_path(
            r"^findbysimulator$(?i)", views.findbysimulator, name="findbysimulator"
        ),
        re_path(r"^publications$(?i)", views.publications, name="publications"),
        re_path(
            r"^(?:mdb)?citations$(?i)",
            views.citations_redirect,
            name="mdbcitations_redirect",
        ),
        re_path(
            r"^citations/(?P<paper_id>.+)$(?i)", views.mdbcitations, name="mdbcitations"
        ),
        re_path(
            r"^models-with-uncurated-references$(?i)",
            views.models_with_uncurated_references,
            name="uncurated",
        ),
        re_path(r"^forget_access$(?i)", views.forget_access, name="forget_access"),
        path(r"rwac-reset/p<slug:code>", views.rwac_reset_p, name="rwac_reset_p"),
        path(r"rwac-reset/<int:model_id>", views.rwac_reset, name="rwac_reset"),
        path(
            r"modelview-data/<slug:item>", views.modelview_data, name="modelview_data"
        ),
        re_path(
            r"^(?P<kind>model)author/(?P<author>.+)$(?i)",
            views.modelauthor,
            name="modelauthor",
        ),
        # path('admin/', admin.site.urls),
        re_path(r"^api/v1/", include(urls_api_v1)),
    ]
    + pipeline_re_path
    + [
        path("change-password", views.change_password),
        path("admin/", admin.site.urls),
        re_path(r"^data/(?P<path>.+)$", views.download_data, name="download_data"),
        path("<int:model_id>", views.showmodel, name="showmodel"),
    ]
)
