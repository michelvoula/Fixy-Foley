from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.utils.html import escape
from forms import get_model_form, normalize_model_name
from django import forms
from medias.forms import *
from salon.models import *
from salon.forms import *
import sys

def add_new_model(request, model_name, form=None):
    normal_model_name = normalize_model_name(model_name)


    photos=Medias.objects.filter(str_type="image")
    
    if request.method == 'POST':
        int_height=request.POST.get('int_height')
        int_width=request.POST.get('int_width')
        if model_name == "ExistingMedia" :
            imgsrc = request.POST.get('imgToAdd')
            img="<img src='"+imgsrc+"'"
            
            if int_width :
                img=img+"width='"+int_width+"'"
            if int_height :
                img=img+"height='"+int_height+"'"
                
            img=img + "alt='' />"
                
            #if form.is_valid():
            if imgsrc:
                return HttpResponse('<script type="text/javascript">opener.updateContent(window, "%s", "%s");</script>' % \
                    (escape('12'), escape(img)))
        else :
            if model_name == "NewMedia" :
                
                #print "OK Form isValid"
                form=ImageForm(request.POST, request.FILES)
                #print form
                if form.is_valid() :
                    #print "OK Form isValid"
                    try:
                        new_obj =form.save(commit=False)
                        new_obj.str_type="image"
                        new_obj.author=request.user
                        new_obj.save()
                    except forms.ValidationError, error:
                        new_obj = None
                    
                    if new_obj:
                        img="<img src='"+new_obj.str_file.url+"' alt=''"
                        if int_width :
                            img=img+"width='"+int_width+"'"
                        if int_height :
                            img=img+"height='"+int_height+"'"
                        img=img + "alt='' />"
                        return HttpResponse('<script type="text/javascript">opener.updateContent(window, "%s", "%s");</script>' % \
                    (escape(new_obj._get_pk_val()), escape(img)))

        

    #else:
        #form = AddPhotoForm()
        
    insertMediaForm=ImageForm()
    page_context = {'form': form, 'field': normal_model_name,"photos":photos,"mediaForm":insertMediaForm}
    return render_to_response('popup.html', page_context, context_instance=RequestContext(request))

def add_new_video(request, video_type, form=None):


    normal_model_name = normalize_model_name(video_type)


    videos=Medias.objects.filter(str_type="video")
    
    if request.method == 'POST':
        int_height=request.POST.get('int_height')
        int_width=request.POST.get('int_width')
        if video_type == "ExistingMedia" :
            videosrc = request.POST.get('videoToAdd')
            video="<embed src='"+videosrc+"' type='application/x-shockwave-flash' name='plugin'"
            
            if int_width :
                video=video+"width='"+int_width+"'"
            if int_height :
                
                video=video+"height='"+int_height+"'"
                
            video=video +"/>"
                
            #if form.is_valid():
            if videosrc:
                return HttpResponse('<script type="text/javascript">opener.updateContent(window, "%s", "%s");</script>' % \
                    (escape('12'), escape(video)))
        else :
            if video_type == "NewMedia" :
                
                #print "OK Form isValid"
                form=ImageForm(request.POST, request.FILES)
                #print form
                if form.is_valid() :
                    #print "OK Form isValid"
                    try:
                        new_obj =form.save(commit=False)
                        new_obj.str_type="image"
                        new_obj.author=request.user
                        new_obj.save()
                    except forms.ValidationError, error:
                        new_obj = None
                    
                    if new_obj:
                        video="<embed src='"+new_obj.str_file.url+"' type='application/x-shockwave-flash' name='plugin'"
                        if int_width :
                            video=video+"width='"+int_width+"'"
                        if int_height :
                            video=video+"height='"+int_height+"'"
                        video=video + "alt='' />"
                        return HttpResponse('<script type="text/javascript">opener.updateContent(window, "%s", "%s");</script>' % \
                    (escape(new_obj._get_pk_val()), escape(video)))
            else :
                    if video_type == "WebMedia" :
                        form=WebVideoForm(request.POST)
                        if form.is_valid():
                            try:
                                new_obj =form.save(commit=False)
                                new_obj.str_type="video_url"
                                new_obj.author=request.user
                                new_obj.save()
                            except forms.ValidationError, error:
                               # print "an error occurs"
                                new_obj=None
                        if new_obj :
                            video=new_obj.str_embed_code
                            return HttpResponse('<script type="text/javascript">opener.updateContent(window, "%s", "%s");</script>' % \
                    (escape(new_obj._get_pk_val()), escape(video))) 
                                
                    

    
    #else:
        #form = AddPhotoForm()
        
    insertMediaForm=ImageForm()
    #print insertMediaForm
    webVideoForm=WebVideoForm()
    page_context = {'form': form, 'field': normal_model_name,"videos":videos,"mediaForm":insertMediaForm,"webVideoForm":webVideoForm}
    return render_to_response('video_popup.html', page_context, context_instance=RequestContext(request))


def add_new_album(request, model_name, form=None):
    


    album_photos=MediaAlbum.objects.filter(str_type="image")
    album_videos=MediaAlbum.objects.filter(str_type="video")
    
    if request.method == 'POST':

        type= ""
        if model_name == "Photo" :
            type="display_photo_album"
        else :
            if model_name == "Video" :
                type="display_video_album"
        
        print type
        imgsrc = request.POST.get('albumToAdd')
            
        album=MediaAlbum.objects.get(pk=imgsrc)
        int_height=album.medias.count()
        int_height=75*int_height+250
        int_width=600
        img="<iframe frameBorder=\"0\" src='/"+type+"/"+imgsrc+"'/"
            
        if int_width :
            img=img+"width='"+str(int_width)+"'"
        if int_height :
            print int_height
                
            img=img+"height='"+str(int_height)+"'"
                
            img=img + "></iframe>"
                
            #if form.is_valid():
            if imgsrc:
                return HttpResponse('<script type="text/javascript">opener.updateContent(window, "%s", "%s");</script>' % \
                    (escape('12'), escape(img)))
        
    page_context = {'albums': album_photos,'videos':album_videos}
    
    return render_to_response('album_popup.html', page_context, context_instance=RequestContext(request))
    
    
    