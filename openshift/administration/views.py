from django.shortcuts import render_to_response,get_object_or_404
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login,logout
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from salon.models import  *
from salon.forms import  *
from django.contrib.auth.decorators import login_required

def index(request):
    template="administration/auth.html"
    page_context={"template":"default",}
    return render_to_response(template,page_context, context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/administration/")
    

def login_user(request):
    state = "Please log in below..."
    template="administration/auth.html"
    username = password = ''
    redirect = request.GET.get('next','') 
    
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        redirect = request.POST.get('next') 
        
        user=None
        
        #print username;
        #print password;
        try :
            user=User.objects.get(email=username);
            if user is not None:
                user=authenticate(username=user.username,password=password)
            else :
                user = authenticate(username=username, password=password)
        except :
            user = authenticate(username=username, password=password)
            state="user is none"
        if user is not None:
     
            if user.is_active:
                login(request, user)
                
                
                if redirect:
                    return HttpResponseRedirect(redirect) 
                    
                return HttpResponseRedirect("/administration/dashboard/")                
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    page_context={"state":state,"next":redirect}
    return render_to_response(template,page_context, context_instance=RequestContext(request))  

@login_required
def dashboard(request):
    adminrole=AdminRole.objects.all()
        
    admins=SalonAdmin.objects.filter(role=adminrole)
    
    template="administration/dashboard.html"
    
    stylists=Stylist.objects.filter(salon__administrator__user__id=request.user.id)[:10]
        
    salons=Salon.objects.filter(administrator__user__id=request.user.id)[:10]
    
    services=SalonService.objects.filter(salon__administrator__user__id=request.user.id)[:10]
    
    page_context={"admins":admins,"salons":salons,"stylists":stylists,"services":services}
    
    return render_to_response(template,page_context, context_instance=RequestContext(request)) 

@login_required   
def view_users(request):
    roles=AdminRole.objects.all()
    template="administration/admin/permissions.html"
    page_context={"roles":roles}
    return render_to_response(template,page_context, context_instance=RequestContext(request)) 
@login_required
def view_admin(request,user_id):
    roles=AdminRole.objects.all()
    admin_user=get_object_or_404(SalonAdmin, pk=user_id)
    template="administration/admin/detail.html"
    page_context={"roles":roles,"admin_user":admin_user}
    return render_to_response(template,page_context, context_instance=RequestContext(request)) 
@login_required    
def add_admin(request):
    user_form=SalonAdminUserForm(prefix="user")
    admin_user_form=SalonAdminForm(prefix="compl")
    
    
    roles=AdminRole.objects.all()
        
    if request.POST:
        user_form=SalonAdminUserForm(request.POST,prefix="user")
        admin_user_form=SalonAdminForm(request.POST,prefix="compl")
        
        if user_form.is_valid() and admin_user_form.is_valid():
            
            user=user_form.save()
            
            user.save()
            
            admin_user=admin_user_form.save(commit=False)
            admin_user.user=user
            admin_user.save()
            
            service_priv=int(request.POST.get("service_priv"))
            
            
            add_permission=Permission.objects.filter(codename="add_salonservice")
            edit_permission=Permission.objects.filter(codename="change_salonservice")
            view_permission=Permission.objects.filter(codename="view_salonservice")
            delete_permission=Permission.objects.filter(codename="delete_salonservice")
            
            #print view_permission[0]
            if service_priv >= 2:
                               
                user.user_permissions.add(view_permission[0])
                if service_priv == 3:
                    user.user_permissions.add(edit_permission[0])
                    user.user_permissions.add(delete_permission[0])
                    user.user_permissions.add(add_permission[0])
            user.set_password(request.POST.get("user-password"))                   
            user.save()
            
            return HttpResponseRedirect("/administration/users/")
                            
    template="administration/admin/add.html"
    page_context={"user_form":user_form,"admin_user_form":admin_user_form,"roles":roles}
    
    return render_to_response(template,page_context, context_instance=RequestContext(request)) 
@login_required      
def edit_admin(request,user_id):
    admin_user=get_object_or_404(SalonAdmin, pk=user_id)
    user_form=SalonAdminUserForm(instance=admin_user.user,prefix="user")
    admin_user_form=SalonAdminForm(instance=admin_user,prefix="compl")
    roles=AdminRole.objects.all()
        
    if request.POST:
        user_form=SalonAdminUserForm(request.POST,instance=admin_user.user,prefix="user")
        admin_user_form=SalonAdminForm(request.POST,instance=admin_user,prefix="compl")
        
        if user_form.is_valid() and admin_user_form.is_valid():
            
            user=user_form.save()
            user.set_password(request.POST.get("user-password")) 
            admin_user=admin_user_form.save(commit=False)
            
            
            
            
            service_priv=int(request.POST.get("service_priv"))
            add_permission=Permission.objects.filter(codename="add_salonservice")
            edit_permission=Permission.objects.filter(codename="change_salonservice")
            view_permission=Permission.objects.filter(codename="view_salonservice")
            delete_permission=Permission.objects.filter(codename="delete_salonservice")
            print view_permission[0].id
            print service_priv
            if service_priv >= 2:
                               
                user.user_permissions.add(view_permission[0])
                if service_priv == 3:
                    user.user_permissions.add(edit_permission[0])
                    user.user_permissions.add(delete_permission[0])
                    user.user_permissions.add(add_permission[0])
                else :
                    user.user_permissions.remove(edit_permission[0])
                    user.user_permissions.remove(delete_permission[0])
                    user.user_permissions.remove(add_permission[0])                   
                
            #else:
                #user.user_permissions.remove(add_permission[0])
            salon_priv=int(request.POST.get("salon_priv"))
            add_permission=Permission.objects.filter(codename="add_salon")
            edit_permission=Permission.objects.filter(codename="change_salon")
            view_permission=Permission.objects.filter(codename="view_salon")
            delete_permission=Permission.objects.filter(codename="delete_salon")
            if salon_priv >= 2:
                               
                user.user_permissions.add(view_permission[0])
                if salon_priv == 3:
                    user.user_permissions.add(edit_permission[0])
                    user.user_permissions.add(delete_permission[0])
                    user.user_permissions.add(add_permission[0])
                else :
                    user.user_permissions.remove(edit_permission[0])
                    user.user_permissions.remove(delete_permission[0])
                    user.user_permissions.remove(add_permission[0])                   
                
            #else:
                #user.user_permissions.remove(add_permission[0])
                
            user.save()
            return HttpResponseRedirect("/administration/users/")
                
    salon_priv=1 
    if admin_user.user.has_perm("salon.view_salon"):
        salon_priv=2
        if admin_user.user.has_perm("salon.change_salon"):
            salon_priv=3
    service_priv=1 
    
    if admin_user.user.has_perm("salon.view_salonservice"):
        service_priv=2
    if admin_user.user.has_perm("salon.change_salonservice"):
        service_priv=3
        
    print service_priv
    template="administration/admin/edit.html"
    page_context={"user_form":user_form,"admin_user_form":admin_user_form,"roles":roles,"admin_user":admin_user,"salon_priv":salon_priv,"service_priv":service_priv}
    
    return render_to_response(template,page_context, context_instance=RequestContext(request)) 
@login_required       
def delete_admin(request,user_id):
    
    admin_user=get_object_or_404(SalonAdmin, pk=user_id)
    admin_user.delete()
    admin_user.user.delete()
    return HttpResponseRedirect("/administration/users/")