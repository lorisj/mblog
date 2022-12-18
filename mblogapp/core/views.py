from django.shortcuts import render

from blog.models import Mblock

# Create your views here.


def frontpage(request):
    featured_Mblocks = Mblock.objects.all()
    # 
    return render(request, "core/frontpage.html", {'featured_Mblocks': featured_Mblocks})

def about(request):
    return render(request, "core/about.html")

