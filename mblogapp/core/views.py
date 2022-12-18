from django.shortcuts import render

from blog.models import Mblock

# Create your views here.


def about(request):
    return render(request, "core/about.html")

