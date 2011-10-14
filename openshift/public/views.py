from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login,logout
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def err400(request):
    template="400.html"
    page_context={"template":template,}
    return render_to_response(template,page_context, context_instance=RequestContext(request))
def err500(request):
    template="500.html"
    page_context={"template":template,}
    return render_to_response(template,page_context, context_instance=RequestContext(request))
def index(request):
    template="index.html"
    page_context={"template":"default",}
    return render_to_response(template,page_context, context_instance=RequestContext(request))
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
    

def login_user(request):
    state = "Please log in below..."
    template="index.html"
    salon = None
    username = password = ''
    client_id=''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
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
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    page_context={"state":state}
    return render_to_response(template,page_context, context_instance=RequestContext(request))  


