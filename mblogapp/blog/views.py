from django.shortcuts import get_object_or_404,render
from .models import Mblock

# Create your views here.

def frontpage(request):
    featured_Mblocks = Mblock.objects.all()
    
    return render(request, "blog/frontpage.html", {'featured_Mblocks': featured_Mblocks})


def detail(request, slug_in):
    mblock = get_object_or_404(Mblock, slug=slug_in)

    return render(request, "blog/detail.html", {"mathblock" : mblock})