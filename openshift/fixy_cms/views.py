# Create your views here.
from django.shortcuts import render_to_response
from fixy_cms.forms import *
from medias.models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def createpost(request):
    photos=Medias.objects.filter(str_type="image")
    return render_to_response('post/add_image.html', {'photos': photos})

def insertImage(request):
    photos=Medias.objects.filter(str_type="image")
    return render_to_response('post/add_image.html', {'photos': photos})
    
def display_post(request,post_id):
    post=get_object_or_404(Post, pk=post_id)
    template="default"
    if post.template:
        template=post.template.str_name
        
    return render_to_response('post_templates/'+template+'/template.html', {'post': post})
