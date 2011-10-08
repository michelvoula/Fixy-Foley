from django.shortcuts import render_to_response, get_object_or_404
from models import Salon,Stylist
from django.template import RequestContext
import sys
from django.http import HttpResponse
from django.utils.html import escape
from forms import *
from django.http import HttpResponseRedirect
# ...

def add_stylist(request,salon_id, form=None):
    form=StylistForm()
    p=request.session['salon'] 
    if request.method == 'POST':
        form=StylistForm(request.POST, request.FILES)
        if form.is_valid() :
            try:
                if p == None :
                    p = get_object_or_404(Salon, pk=salon_id)
                new_obj =form.save(commit=False)
                new_obj.salon=p
                #new_obj.author=request.user
                new_obj.save()
            except forms.ValidationError, error:
                #print "Exception in user code:"
                #print '-'*60
                new_obj = None
        
            #print "form non valid"
    page_context = {'form': form,"salon":p}
    return render_to_response('stylist/add.html', page_context, context_instance=RequestContext(request))
def userSalons(request, user_id):
    salons=Salon.objects.get(administrator_id=user_id)
    salon=None
    if salons :
        salon=salons[0]
    
        
    page_context={"salons":salons,"salon":salon}
    return render_to_response('salon/detail.html',page_context, context_instance=RequestContext(request))
def detail(request, salon_id):
    
    if salon_id == 0:
        p=request.session['salon']
    else:
        p = get_object_or_404(Salon, pk=salon_id)
    request.session['salon'] = p
    form=SalonPhotoForm(instance=p)
    page_context={"salon":p,"form":form}
    return render_to_response('salon/detail.html',page_context, context_instance=RequestContext(request))  
def stylist(request, salon_id):
    p = get_object_or_404(Salon, pk=salon_id)
    request.session['salon'] = p
    page_context={"salon":p}
    return render_to_response('stylist/stylists.html', page_context, context_instance=RequestContext(request))
def stylistview(request, stylist_id):
    stylist = get_object_or_404(Stylist, pk=stylist_id)
    salon=stylist.salon
    page_context={"salon":salon,'stylist': stylist,}
    return render_to_response('salon/detail.html', page_context, context_instance=RequestContext(request))

def edit_salon_photo(request,salon_id,form=None):
    salon =get_object_or_404(Salon, pk=salon_id)
    if request.method == 'POST':
        form=SalonPhotoForm(request.POST, request.FILES,instance=salon)
        if form.is_valid(): 
            #print "ok dss"       
            salon =form.save()
            #salon.img_photo =request.POST.get("img_photo")
        
          
    
    form=SalonPhotoForm(instance=salon)
    page_context={"salon":salon,"form":form}
    #return render_to_response('salon/detail.html',page_context, context_instance=RequestContext(request))  
    return HttpResponseRedirect("/salon/"+str(salon.id))


def add_salon(request,form=None):
    if request.method == 'POST':
        form=SalonForm(request.POST)
        if form.is_valid(): 
            #print "ok dss"       
            salon =form.save()
            return HttpResponseRedirect("/salon/"+str(salon.id))
            #salon.img_photo =request.POST.get("img_photo")
        
    form=SalonForm()
    page_context={"form":form}
    return render_to_response('salon/add.html',page_context, context_instance=RequestContext(request))  

def edit_salon(request,salon_id,form=None):
    salon =get_object_or_404(Salon, pk=salon_id)
    form=SalonForm(instance=salon)
    if request.method == 'POST':
        form=SalonForm(request.POST, instance=salon)
        if form.is_valid(): 
            #print "ok dss"       
            salon =form.save()
            return HttpResponseRedirect("/salon/"+str(salon.id))
            #salon.img_photo =request.POST.get("img_photo")
        
          
    
    
    page_context={"salon":salon,"form":form}
    return render_to_response('salon/edit.html',page_context, context_instance=RequestContext(request))  
    
def salon_services(request,salon_id):
    salon =get_object_or_404(Salon, pk=salon_id)
    services=SalonService.objects.filter(salon=salon_id)
    form=None
    service=None
    if services:
        service=services[0]
        form=SalonServiceForm(instance=service)
        #print service
    
    page_context={"salon":salon,"service":service,"form":form}
    return render_to_response('service/edit.html',page_context, context_instance=RequestContext(request))  



def delete_salon_service(request,service_id,form=None):
    service =get_object_or_404(SalonService, pk=service_id)
    salon=service.salon    
    service.delete()
    return HttpResponseRedirect("/salon/"+str(salon.id))


def edit_salon_service(request,service_id,form=None):
    service =get_object_or_404(SalonService, pk=service_id)
    salon=service.salon
    form=SalonServiceForm(instance=service)
    if request.method == 'POST':
        form=SalonServiceForm(request.POST, instance=service)
        if form.is_valid(): 
            #print "ok dss"       
            service =form.save()
            return HttpResponseRedirect("/salon/"+str(salon.id))
            #salon.img_photo =request.POST.get("img_photo")
        
          
    
    
    page_context={"salon":salon,"service":service,"form":form}
    return render_to_response('service/edit.html',page_context, context_instance=RequestContext(request))  
    
def add_salon_service(request,salon_id,form=None):
    service =None
    salon =get_object_or_404(Salon, pk=salon_id)
    form=SalonServiceForm()
    if request.method == 'POST':
        form=SalonServiceForm(request.POST)
        if form.is_valid(): 
            #print "ok dss"       
            service =form.save(commit=False)
            service.salon=salon
            service.save()
            return HttpResponseRedirect("/salon/"+str(salon.id))
            #salon.img_photo =request.POST.get("img_photo")
        
          
    
    
    page_context={"salon":salon,"form":form}
    return render_to_response('service/add.html',page_context, context_instance=RequestContext(request))  


def add_job(request,pop_up):
    form=JobTitleForm()
    if request.method == 'POST':
            form=JobTitleForm(request.POST)
            if form.is_valid(): 
                job =form.save()
                if pop_up:
                    return HttpResponse('<script type="text/javascript">window.close();opener.updateCombo("%s", "%s", "%s");</script>' % \
                    (escape(pop_up),escape(job.id), escape(job.str_name)))
    page_context={"form":form}
    return render_to_response('stylist/add_job.html',page_context, context_instance=RequestContext(request))  
       
def add_service(request,pop_up):
    form=ServiceForm()
    if request.method == 'POST':
            form=ServiceForm(request.POST)
            if form.is_valid(): 
                service =form.save()
                #if pop_up:
                    #return HttpResponseRedirect("/salon/"+str(salon.id))
    page_context={"form":form}
    return render_to_response('service/add_type.html',page_context, context_instance=RequestContext(request))  
        
        
def salon_team(request,salon_id):
    salon =get_object_or_404(Salon, pk=salon_id)
    stylists=Stylist.objects.filter(salon=salon_id)
    form=None
    stylist=None
    if stylists:
        stylist=stylists[0]
        form=StylistForm(instance=stylist)
        #print service
    
    page_context={"salon":salon,"stylist":stylist,"form":form}
    return render_to_response('stylist/edit.html',page_context, context_instance=RequestContext(request))  


def add_salon_stylist(request,salon_id,form=None):
    service =None
    salon =get_object_or_404(Salon, pk=salon_id)
    form=StylistForm()
    if request.method == 'POST':
        form=StylistForm(request.POST)
        if form.is_valid(): 
            #print "ok dss"       
            stylist =form.save(commit=False)
            stylist.salon=salon
            stylist.save()
            return HttpResponseRedirect("/salon/stylist/"+str(salon.id))
            #salon.img_photo =request.POST.get("img_photo")
def edit_salon_stylist(request,stylist_id,form=None):
    stylist =get_object_or_404(Stylist, pk=stylist_id)
    salon=stylist.salon
    form=StylistForm(instance=stylist)
    if request.method == 'POST':
        form=StylistForm(request.POST, instance=stylist)
        if form.is_valid(): 
            #print "ok dss"       
            stylist =form.save()
            return HttpResponseRedirect("/salon/"+str(salon.id))
            #salon.img_photo =request.POST.get("img_photo")    
    page_context={"salon":salon,"stylist":stylist,"form":form}
    return render_to_response('stylist/edit.html',page_context, context_instance=RequestContext(request))  

def edit_stylist_photo(request,stylist_id,form=None):
    stylist =get_object_or_404(Stylist, pk=stylist_id)
    if request.method == 'POST':
        form=StylistPhotoForm(request.POST, request.FILES,instance=stylist)
        if form.is_valid(): 
            #print "ok dss"       
            salon =form.save()
            #salon.img_photo =request.POST.get("img_photo")
        
          
    
    form=StylistPhotoForm(instance=salon)
    page_context={"stylist":stylist,"form":form}
    #return render_to_response('salon/detail.html',page_context, context_instance=RequestContext(request))  
    return HttpResponseRedirect("/stylist/"+str(stylist.id))
  
def delete_salon_stylist(request,stylist_id):    
    #delete salon stylist
    stylist =get_object_or_404(Stylist, pk=stylist_id)    
    salon=stylist.salon    
    #delete the stylist
    stylist.delete()
    return HttpResponseRedirect("/salon/"+str(salon.id))    