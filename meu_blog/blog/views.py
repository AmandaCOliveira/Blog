from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.template import RequestContext
from blog.models import Artigo
# Create your views here.

def blog(request):
    a = 'Amanda'
    artigo = Artigo.objects.all()
    return render_to_response(
        'blog/index.html',
        locals(), 
        context_instance = RequestContext(request)
    )


