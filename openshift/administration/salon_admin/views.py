from django.shortcuts import render_to_response, get_object_or_404
from salon.models import Salon,Stylist
from django.template import RequestContext
import sys
from django.http import HttpResponse
from django.utils.html import escape
from salon.forms import *
from django.http import HttpResponseRedirect
from decimal import Decimal
from django.contrib.auth.decorators import login_required
# ...
@login_required  
def delete_salon(request,salon_id):    
    #delete salon stylist
    salon =get_object_or_404(Salon, pk=salon_id)    
    salon.delete()
    return HttpResponseRedirect("/administration/salon/user/"+str(request.user.id))   

@login_required  
def delete_salon_stylist(request,stylist_id):    
    #delete salon stylist
    stylist =get_object_or_404(Stylist, pk=stylist_id)    
    salon=stylist.salon    
    #delete the stylist
    stylist.delete()
    return HttpResponseRedirect("/administration/salon/"+str(salon.id))
@login_required 
def userServices(request, user_id):
    
    salons=SalonManager.objects.filter(admin__user__id=user_id)
    salon=None
    if salons :
        salon=salons[0]
        return HttpResponseRedirect("/administration/salon/service/"+str(salon.salon.id))
    else:
        form=SalonForm()
        page_context={"form":form}
        return render_to_response('administration/salon/add.html',page_context, context_instance=RequestContext(request))  


@login_required 
def userStylists(request, user_id):
    
    salons=SalonManager.objects.filter(admin__user__id=user_id)
    salon=None
    if salons :
        salon=salons[0]
        return HttpResponseRedirect("/administration/salon/stylist/"+str(salon.salon.id))
    else:
        form=SalonForm()
        page_context={"form":form}
        return render_to_response('administration/salon/add.html',page_context, context_instance=RequestContext(request))  

@login_required 
def userSalons(request, user_id):
    
    salons=SalonManager.objects.filter(admin__user__id=user_id)
    salon=None
    if salons :
        salon=salons[0]
        return HttpResponseRedirect("/administration/salon/"+str(salon.salon.id))
    else:
        form=SalonForm()
        page_context={"form":form}
        return render_to_response('administration/salon/add.html',page_context, context_instance=RequestContext(request))  
@login_required 
def detail(request, salon_id):
    #print salon_id
    #salons=SalonManager.objects.filter(admin=request.user.id)
    p=None
    if salon_id == "0":
        form=SalonForm()
        #page_context={"form":form}
        #return render_to_response('administration/salon/add.html',page_context, context_instance=RequestContext(request))  
    else:
        p = get_object_or_404(Salon, pk=salon_id)
    request.session['salon'] = p
    form=SalonPhotoForm(instance=p)
    page_context={"salon":p,"form":form}
    return render_to_response('administration/salon/detail.html',page_context, context_instance=RequestContext(request))  

@login_required 
def stylist(request, salon_id):
    p = get_object_or_404(Salon, pk=salon_id)
    request.session['salon'] = p
    page_context={"salon":p}
    return render_to_response('administration/stylist/stylists.html', page_context, context_instance=RequestContext(request))

@login_required 
def stylistview(request, stylist_id):
    stylist = get_object_or_404(Stylist, pk=stylist_id)
    photo_form =StylistPhotoForm(instance=stylist)
    salon=stylist.salon
    page_context={"salon":salon,'stylist': stylist,"photo_form":photo_form}
    return render_to_response('administration/salon/detail.html', page_context, context_instance=RequestContext(request))

@login_required 
def edit_salon_photo(request,salon_id,form=None):
    salon =get_object_or_404(Salon, pk=salon_id)
    #print "before" +    salon.img_photo.url
    if request.method == 'POST':
        form=SalonPhotoForm(request.POST, request.FILES,instance=salon)
        if form.is_valid(): 
             
            salon =form.save()
            #print "after" +    salon.img_photo.url
            #salon.img_photo =request.POST.get("img_photo")
    return HttpResponseRedirect("/administration/salon/edit/"+str(salon.id))
@login_required 
def edit_stylist_photo(request,stylist_id,form=None):
    stylist =get_object_or_404(Stylist, pk=stylist_id)
    if request.method == 'POST':
        form=StylistPhotoForm(request.POST, request.FILES,instance=stylist)
        print request.POST.get("img_photo") 
        if form.is_valid(): 
                 
            stylist =form.save()
    return HttpResponseRedirect("/administration/salon/stylist/edit/"+str(stylist.id))

@login_required 
def add_salon(request,form=None):
    day_form_list=list()
    for day in DAYS_OF_WEEK:
        hform=OpeningHourForm(prefix="hof"+str(day[0]))
        day_form_list.append((day,hform))
    form=SalonForm()   
   
    
    if request.method == 'POST':
        valid_forms=True
        day_form_list=list()
        for day in DAYS_OF_WEEK:
            hform=OpeningHourForm(request.POST,prefix="hof"+str(day[0]))
            day_form_list.append((day,hform))
            if not hform.is_valid():
                valid_forms=False
                
        form=SalonForm(request.POST)
        if form.is_valid() and  valid_forms: 
            #print "ok dss" 
                
            salon =form.save()
            salonManager=SalonManager()
            salonManager.salon=salon
            salonManager.admin=salon.administrator
            salonManager.save()
            
            for hl in day_form_list:
                hform=hl[1]
                day=hl[0]
                hday=hform.save(commit=False)
                hday.salon=salon
                hday.day=day[0]
                hday.save()
                
            
            return HttpResponseRedirect("/administration/salon/"+str(salon.id))
            #salon.img_photo =request.POST.get("img_photo")
        
    
    page_context={"form":form,"days_of_week":DAYS_OF_WEEK,"day_form_list":day_form_list}
    return render_to_response('administration/salon/add.html',page_context, context_instance=RequestContext(request))  
    
@login_required 
def edit_salon(request,salon_id,form=None):
    salon =get_object_or_404(Salon, pk=salon_id)
    form=SalonForm(instance=salon)
    photo_form=SalonPhotoForm(instance=salon)
    
    day_form_list=list()
    for day in DAYS_OF_WEEK:
        hdays=OpeningHour.objects.filter(salon__id=salon.id,day=day[0])
        if hdays:
            hday=hdays[0]
            hform=OpeningHourForm(prefix="hof"+str(day[0]),instance=hday)
            day_form_list.append((day,hform))
        
    if request.method == 'POST':
        form=SalonForm(request.POST, instance=salon)
        valid_forms=True
        day_form_list=list()
        for day in DAYS_OF_WEEK:
            hdays=OpeningHour.objects.filter(salon__id=salon.id,day=day[0])
            if hdays:
                hday=hdays[0]
                hform=OpeningHourForm(request.POST,prefix="hof"+str(day[0]),instance=hday)
                day_form_list.append((day,hform))
                if not hform.is_valid():
                    valid_forms=False
        
        if form.is_valid() and valid_forms: 
            #print "ok dss"       
            salon =form.save()
            
            salonManager=SalonManager.objects.filter(admin__id=salon.administrator.id,salon__id=salon.id)
            
            
            for hl in day_form_list:
                hform=hl[1]
                day=hl[0]
                hday=hform.save()                
            
            if not salonManager :
                
                salonManager=SalonManager()
                salonManager.salon=salon
                salonManager.admin=salon.administrator
                salonManager.save()
                
            
            return HttpResponseRedirect("/administration/salon/"+str(salon.id))
            #salon.img_photo =request.POST.get("img_photo")
                
    page_context={"salon":salon,"form":form,"photo_form":photo_form,"day_form_list":day_form_list}
    return render_to_response('administration/salon/edit.html',page_context, context_instance=RequestContext(request))  

@login_required    
def salon_services(request,salon_id):
    salon =get_object_or_404(Salon, pk=salon_id)
    services=SalonService.objects.filter(salon=salon_id)
    form=None
    service=None
    if services:
        service=services[0]
        form=SalonServiceForm(instance=service)
        return HttpResponseRedirect("/administration/salon/service/view/"+str(service.id))
    else :
        return HttpResponseRedirect("/administration/salon/service/add/"+str(salon.id))
        
        #print service
    
    
     


@login_required 
def delete_salon_service(request,service_id,form=None):
    service =get_object_or_404(SalonService, pk=service_id)
    salon=service.salon    
    service.delete()
    return HttpResponseRedirect("/administration/salon/"+str(salon.id))

@login_required 
def view_salon_service(request,service_id,form=None):
    service =get_object_or_404(SalonService, pk=service_id)
    salon=service.salon
    form=SalonServiceForm(instance=service)                
    page_context={"salon":salon,"service":service,"form":form}
    return render_to_response('administration/service/detail.html',page_context, context_instance=RequestContext(request))  

@login_required 
def edit_salon_service(request,service_id,form=None):
    service =get_object_or_404(SalonService, pk=service_id)
    salon=service.salon
    form=SalonServiceForm(instance=service)
    if request.method == 'POST':
        form=SalonServiceForm(request.POST, instance=service)
        if form.is_valid(): 
            #print "ok dss"       
            service =form.save()
            return HttpResponseRedirect("/administration/salon/service/view/"+str(service.id)+"/")
            #salon.img_photo =request.POST.get("img_photo")
        
          
    
    
    page_context={"salon":salon,"service":service,"form":form}
    return render_to_response('administration/service/edit.html',page_context, context_instance=RequestContext(request))  

@login_required   
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
            return HttpResponseRedirect("/administration/salon/service/"+str(salon.id)+"/")
            #salon.img_photo =request.POST.get("img_photo")
        
          
    
    
    page_context={"salon":salon,"form":form}
    return render_to_response('administration/service/add.html',page_context, context_instance=RequestContext(request))  

@login_required 
def add_job(request,pop_up):
    form=JobTitleForm()
    if request.method == 'POST':
            form=JobTitleForm(request.POST)
            if form.is_valid(): 
                job =form.save()
                if pop_up:
                    return HttpResponse('<script type="text/javascript">window.close();opener.updateCombo("%s", "%s", "%s");</script>' % \
                    (escape("id_primary-jobTitle"),escape(job.id), escape(job.str_name)))
    page_context={"form":form}
    return render_to_response('administration/stylist/add_job.html',page_context, context_instance=RequestContext(request))  

@login_required       
def add_service(request,pop_up):
    form=ServiceForm()
    if request.method == 'POST':
            form=ServiceForm(request.POST)
            if form.is_valid(): 
                service =form.save()
                if pop_up:
                    return HttpResponse('<script type="text/javascript">window.close();</script>')
                    #return HttpResponse('<script type="text/javascript">window.close();opener.updateCombo("%s", "%s", "%s");</script>' % \
                    #(escape(pop_up),escape(service.id), escape(service.str_name)))
    page_context={"form":form}
    return render_to_response('administration/service/add_type.html',page_context, context_instance=RequestContext(request))  
 
@login_required        
def salon_service_form(request):    
    if request.POST:
        salon_id=int(request.POST.get("salon_id"))
        return HttpResponseRedirect("/administration/salon/service/"+str(salon_id)+"/")
          
@login_required        
def salon_teams(request):
    
    
    if request.POST:
        salon_id=int(request.POST.get("salon_id"))
        return HttpResponseRedirect("/administration/salon/stylist/"+str(salon_id)+"/")
    
@login_required   
def salon_team(request,salon_id):
    salon =get_object_or_404(Salon, pk=salon_id)
    stylists=Stylist.objects.filter(salon=salon_id)
    form=None
    stylist=None
    photo_form=None
    if stylists:
        stylist=stylists[0]
        form=StylistForm(instance=stylist)
        photo_form =StylistPhotoForm(instance=stylist)
        page_context={"salon":salon,"stylist":stylist,"form":form,"photo_form":photo_form}
        return HttpResponseRedirect("/administration/salon/stylist/view/"+str(stylist.id))
    else:
        return HttpResponseRedirect("/administration/salon/stylist/add/"+str(salon_id))

@login_required 
def stylist_view(request,stylist_id):
    stylist=get_object_or_404(Stylist, pk=stylist_id)
    salon =stylist.salon
    discount_types=DiscountType.objects.filter(stylist=stylist_id)
    discount_type=None
    photo_form =StylistPhotoForm(instance=stylist)
    if discount_types:
        #if discount exists
        discount_type=discount_types[0]   
        #print   discount_type.type   

    page_context={"salon":salon,"stylist":stylist,"discount_type":discount_type,"photo_form":photo_form}
    return render_to_response('administration/stylist/detail.html',page_context, context_instance=RequestContext(request))   


@login_required 
def add_salon_stylist(request,salon_id,form=None):
    service =None
    salon =get_object_or_404(Salon, pk=salon_id)   
    ####edit salon stylist
    
   
    ##build the form
    form=StylistForm(prefix = "primary")
    ##build the photo form
    photo_form =StylistPhotoForm()
    
    ##build the discount form by default
    discount_type_form=DiscountTypeForm(prefix = "discount")
    #print discount_type_form
     
    if request.POST:
        form=StylistForm(request.POST,prefix = "primary")
        discount_type_form=None
        
        discount_type_form=DiscountTypeForm(request.POST,prefix = "discount")        
        serviceList=request.POST.get("serviceList")
        
        if form.is_valid() and discount_type_form.is_valid(): 
            #print "ok dss"       
            stylist =form.save(commit=False)
            stylist.salon=salon
            stylist.save()
            stylist.services=list()
            try :
                listidx = serviceList.split(',')
                for l in listidx:
                    service =get_object_or_404(SalonService, pk=l)
                    stylist.services.add(service)
            except Exception:
                listidx=None
                
            
            
            discount_type=discount_type_form.save(commit=False)
            discount_type.stylist=stylist           
            discount_type.save()
            stylist.save()
                
            return HttpResponseRedirect("/administration/salon/stylist/"+str(salon.id))
    
    page_context={"salon":salon,"form":form,"photo_form":photo_form,"discount_type_form":discount_type_form}
    return render_to_response('administration/stylist/add.html',page_context, context_instance=RequestContext(request))  
 

@login_required 
def edit_salon_stylist(request,stylist_id,form=None):
    
    ####edit salon stylist
    
    #get the stylist
    stylist =get_object_or_404(Stylist, pk=stylist_id)
    salon=stylist.salon
    ##build the form
    form=StylistForm(instance=stylist,prefix = "primary")
    ##build the photo form
    photo_form =StylistPhotoForm(instance=stylist)
    
    ##build the discount form by default
    discount_type_form=DiscountTypeForm(prefix = "discount")
    #print discount_type_form
    
    ##find the discount object of the stylist
    discount_types=DiscountType.objects.filter(stylist=stylist_id)
    discount_type=None
    if discount_types:
        #if discount exists
        discount_type=discount_types[0]    
        discount_type_form=DiscountTypeForm(instance=discount_type,prefix = "discount")
        
        
    if request.method == 'POST':
        form=StylistForm(request.POST, instance=stylist,prefix = "primary")
        discount_type_form=None
        if discount_type == None:
            discount_type=DiscountType()
            discount_type_form=DiscountTypeForm(request.POST,prefix = "discount")
        else:
            discount_type_form=DiscountTypeForm(request.POST,instance=discount_type,prefix = "discount")
        
        serviceList=request.POST.get("serviceList")
        
        if form.is_valid() and discount_type_form.is_valid(): 
            #print "ok dss"       
            stylist =form.save()
            stylist.services=list()
            try :
                listidx = serviceList.split(',')
                for l in listidx:
                    service =get_object_or_404(SalonService, pk=l)
                    stylist.services.add(service)
            except Exception:
                listidx=None
                
            
            
            discount_type=discount_type_form.save(commit=False)
            #print discount_type.type
            discount_type.stylist=stylist           
            discount_type.save()
            
                 
            
                
            
                     
            
            stylist.save()
                
            return HttpResponseRedirect("/administration/salon/stylist/"+str(salon.id))
       # else:
            #print discount_type_form.errors
            #salon.img_photo =request.POST.get("img_photo")    
    #print discount_type_form
    page_context={"salon":salon,"discount_type":discount_type,"stylist":stylist,"form":form,"photo_form":photo_form,"discount_type_form":discount_type_form}
    return render_to_response('administration/stylist/edit.html',page_context, context_instance=RequestContext(request))


def show_calendar(request):
    template="administration/calendar/index.html"
    page_context={"template":"default",}
    return render_to_response(template,page_context, context_instance=RequestContext(request))  
    