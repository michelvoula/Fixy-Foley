
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from medias.models import MediaAlbum
from django.contrib.auth.models import User

def display_photo_album(request,album_id):

    try :
        album=get_object_or_404(MediaAlbum, pk=album_id)
        #print album
        #MediaAlbum.objects.get(id=album_id)
        
        if album :
            #print "OK HEre"
            #page_context = {'album': album}
            return render_to_response('medias/album_photo.html',{'album': album})

        
        
        
    except :
        album=None
        
def display_video_album(request,album_id):
    try :
        album=get_object_or_404(MediaAlbum, pk=album_id)
        #print album
        #MediaAlbum.objects.get(id=album_id)
        
        if album :
            #print "OK HEre"
            #page_context = {'album': album}
            return render_to_response('medias/album_video.html',{'album': album})

        
        
        
    except :
        album=None
