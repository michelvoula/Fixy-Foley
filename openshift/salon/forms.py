from models import *
from django.forms import *
from django.forms import RadioSelect
from django.utils.translation import ugettext as _

class OpeningHourForm(ModelForm):
    days_of_week=DAYS_OF_WEEK
    class Meta:
        model=OpeningHour
        exclude=('salon','day')

class EditSalonAdminUserForm(ModelForm):
    username=CharField(label=_('Login'),required=True,widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    first_name=CharField(label=_('First Name'),required=True,widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    last_name=CharField(label=_('Last Name'),required=True,widget=forms.TextInput(attrs={'size':'40','class':'text95',"type":"password"}))
    #password=CharField(label=_('Password'),required=True,widget=PasswordInput(attrs={'size':'40','class':'text95',"type":"password"}))
   
    class Meta:
        model=User
        fields = ('username','first_name','last_name','email')

class SalonAdminUserForm(ModelForm):
    username=CharField(label=_('Login'),required=True,widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    first_name=CharField(label=_('First Name'),required=True,widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    last_name=CharField(label=_('Last Name'),required=True,widget=forms.TextInput(attrs={'size':'40','class':'text95',"type":"password"}))
    password=CharField(label=_('Password'),required=True,widget=PasswordInput(attrs={'size':'40','class':'text95',"type":"password"}))
   
    class Meta:
        model=User
        fields = ('username','first_name','last_name','email','password')
        
class SalonAdminForm(ModelForm):
    class Meta:
        model=SalonAdmin
        fields = ('role',)


class JobTitleForm(ModelForm):
    class Meta:
        model=JobTitle

class ServiceForm(ModelForm):
    class Meta:
        model=Service
        exclude=('status',)

class SalonServiceForm(ModelForm):
    discount_type=ChoiceField(label=_('Discount options by service'),choices=SalonService.DISCOUNT_TYPE,required=True,widget=RadioSelect())
    def __init__(self,*args,**kwargs):
        super (ModelForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['service'].queryset = Service.objects.filter(status='active_service')
    
    class Meta:
        model=SalonService
        exclude=('salon',)
        
class SalonForm(ModelForm):
    str_name=CharField(label=_('Salon Name'),required=True,widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    str_description=CharField(label=_('Description'),required=False,widget=forms.Textarea(attrs={'rows':'4','cols':'40','class':'text95'}))
    str_specialities=CharField(label=_('Specialities'),required=False,widget=forms.Textarea(attrs={'rows':'4','cols':'40','class':'text95'}))
       
    class Meta:
        model=Salon
        fields = ('str_name','administrator','str_description','str_specialities','str_adress1','str_adress2','city','str_specialities','str_phone','str_fax','str_email','str_web_adress')

class SalonPhotoForm(ModelForm):
    class Meta:
        model=Salon
        fields=('img_photo',)
class StylistPhotoForm(ModelForm):
    class Meta:
        model=Stylist
        fields=('img_photo',)
class DiscountTypeForm(ModelForm):
    class Meta:
        model=DiscountType
        exclude=('stylist',)
class StylistForm(ModelForm):

    str_first_name=CharField(label=_('First Name'),required=True,widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    str_last_name=CharField(label=_('Last Name'),required=True,widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    #str_specialities=CharField(label=_('Specialities'),required=True,widget=forms.Textarea(attrs={'rows':'4','cols':'40','class':'text95'}))
    str_description=CharField(label=_('Description'),required=True,widget=forms.Textarea(attrs={'rows':'4','cols':'40','class':'text95'}))
   
    #img_photo=CharField(label=_('Photo'),required=True,widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    #str_email=CharField(label=_('Email'),required=True,widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    #str_phone=CharField(label=_('Phone Number'),required=True,widget=forms.TextInput(attrs={'size':'40','class':'text95'}))
    def __init__(self, *args, **kwargs):
        super(StylistForm, self).__init__(*args, **kwargs)        
    class Meta:
        model=Stylist
        fields = ('str_first_name','str_last_name','jobTitle','str_description')