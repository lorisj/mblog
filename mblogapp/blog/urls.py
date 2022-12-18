from django.urls import path

from .views import detail, frontpage


urlpatterns = [
    #path("", frontpage, name="frontpage"),
    path("", frontpage, name="frontpage"),
    path("<slug:slug_in>/", detail, name="mblock_detail"),
]
