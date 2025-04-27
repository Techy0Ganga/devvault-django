from django.urls import path

from . import views

app_name = "generator"

urlpatterns = [
    path("", views.ListPresets.as_view(), name="presetlist"),
    path("addpreset/", views.AddPreset, name='addpreset' ),
    path("<int:pk>/", views.presetDetail.as_view(), name="detailPreset"),
    path("<int:pk>/update/", views.presetUpdate, name="updatePreset"),
    path("<int:pk>/delete/", views.presetDelete, name="deletePreset")
]