from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from salon.models import Salon
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_user(request):
    state = "Please log in below..."
    salon = None
    username = password = ''
    client_id=''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        client_id = request.POST.get('client_id')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                try:
                    salon = Salon.objects.get(pk=client_id)
                    state = "You're successfully logged in! To Salon "+salon.str_name
                except Salon.DoesNotExist:
                    state="You are loggend in But the Salon is unknown"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
        return render_to_response('salon_details.html',{'state':state, 'username': username,'client_id':client_id,"salon":salon})

    return render_to_response('auth.html',{'state':state, 'username': username,'client_id':client_id})