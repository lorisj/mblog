from django.shortcuts import render

from blog.models import Block

# Create your views here.


def frontpage(request):
    featured_blocks = Block.objects.all()
    # 
    return render(request, "core/frontpage.html", {'featured_blocks': featured_blocks})

def about(request):
    return render(request, "core/about.html")

