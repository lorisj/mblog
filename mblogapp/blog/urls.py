from django.urls import path

from . import views

urlpatterns = [
    path("<slug:slug_in>/", views.detail, name="mblock_detail"),
]
