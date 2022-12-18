from django.shortcuts import get_object_or_404,render
from .models import Mblock

# Create your views here.

def detail(request, slug_in):
    mblock = get_object_or_404(Mblock, slug=slug_in)

    return render(request, "blog/detail.html", {"mathblock" : mblock})