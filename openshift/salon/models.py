from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User, Permission

fs = FileSystemStorage(location='/media/photos')
DAYS_OF_WEEK = (
        (1, u'Monday'),
        (2, u'Tuesday'),
        (3, u'Wednesday'),
        (4, u'Thursday'),
        (5, u'Friday'),
        (6, u'Saturday'),
        (7, u'Sunday'),        
    )
class Country(models.Model):
    str_name=models.CharField(max_length=50)
    def __unicode__(self):
        return self.str_name
    
class City(models.Model):
    str_name=models.CharField(max_length=50)
    country = models.ForeignKey(Country)
    def __unicode__(self):
        return self.str_name


class Service(models.Model):
    SERVICE_STATUS_TYPE = (
        (u'waiting_validation', u'Waiting for validation'),
        (u'active_service', u'Active'),      
    )
    str_name=models.CharField(_('Name'),max_length=50)
    str_description=models.TextField(_('Description'),null=True,blank=True,)
    status=models.CharField(_('Status'),max_length=50,null=True,blank=True,choices=SERVICE_STATUS_TYPE)  
    def __unicode__(self):
        return self.str_name

class Salon(models.Model):
    str_owner=models.CharField(_('Salon Manager'),max_length=50,blank=True)
    str_name=models.CharField(_('Salon Name'),max_length=50)
    str_description=models.TextField(_('Description'),blank=True)
    str_specialities=models.TextField(_('Specialities'),blank=True)
    str_adress1=models.CharField(_('Adress Line 1'),max_length=50,blank=True)
    str_adress2=models.CharField(_('Adress Line 2'),max_length=50,blank=True)
    str_fax=models.CharField(_('Fax'),max_length=50,blank=True)
    str_phone=models.CharField(_('Phone'),max_length=50,blank=True)
    str_email=models.EmailField(_('Email'),max_length=50,blank=True)
    str_web_adress=models.URLField(_('Web'),verify_exists=False, max_length=200,blank=True)
    city = models.ForeignKey(City)
    img_photo = models.ImageField(_('Photo'),upload_to='photos',blank=True,default="images/avatar.png")
    administrator=models.ForeignKey("SalonAdmin")
    services = models.ManyToManyField(Service,through='SalonService')
    def __unicode__(self):
        return self.str_name
    class Meta:
        permissions = (
            ("can_administrate_salon", _("Can Administrate the salon")),
            ("can_add_stylist_to_salon", _("Can Add Stylists to salon")),
            ("add_service", _("Add Salon Service")),
            ("is_salon_owner", _("Is salon Owner")),
            ("view_salon",_("View Salons"))
           
        )
def getTimeChoice():
        time=20
        timelist=()
        
        while time < 185:
            m=time%60
            h=time/60
            s=""
            if h>0:
                s=str(h)+" h "+str(m)+" min" 
            else:
                s=str(m)+" min"
            timelist=timelist+((time,s),)
            time=time + 5
            
        return timelist
class JobTitle(models.Model):
    str_name=models.CharField('Name',max_length=50)
    
    def __unicode__(self):
        return self.str_name
class SalonService(models.Model):
    DISCOUNT_TYPE = (
        (u'per_agent', u'Discount as per your team members tier Status'),
        (u'never', u'never discount'),
        (u'exact', u'Always discount at set percentage'),        
    )
    
    service = models.ForeignKey(Service)
    salon=models.ForeignKey(Salon)
    length =models.IntegerField('Length',null=True,blank=True,choices=getTimeChoice())    
    discount_type=models.CharField(_("Type"),max_length=25, choices=DISCOUNT_TYPE,null=True,blank=True)
    discount_percentage=models.DecimalField(_("Percentage"),null=True, blank=True,max_digits=4, decimal_places=2)
    number_appointment=models.IntegerField(_("Number of Appointments"))
    def __init__(self,  *args, **kwargs):
        super(SalonService, self).__init__(*args, **kwargs)
        self._meta.get_field_by_name('length')[0]._choices = getTimeChoice()
    
               
    def __unicode__(self):
        if self.discount_type == 'per_agent':
            return _("Discount as per your team members tier Status")
        else :
            if self.discount_type == 'never':
                return _("Never discount")
            else:
                return _("Always discount at ")+str(self.discount_percentage)+"%"
                
        
    class Meta:
        permissions=(("view_salonservice",_("View Salon Services")),)
        
class OpeningHour(models.Model):
    
    open=models.TimeField(_("Open"),null=True,blank=True,)
    close=models.TimeField(_("Close"),null=True,blank=True,)
    closed=models.BooleanField(_("Closed"))
    salon=models.ForeignKey(Salon)
    day=models.IntegerField('Length',choices=DAYS_OF_WEEK)
         
class Stylist(models.Model):

    str_first_name=models.CharField('First Name',max_length=50)
    str_last_name=models.CharField('Last Name',max_length=50)
    str_position=models.CharField('Position',max_length=50)
    str_specialities=models.TextField('Specialities')
    str_description=models.TextField('Description')
    str_phone=models.CharField('Phone Number',max_length=50)
    str_email=models.EmailField('Email',max_length=50)
    img_photo = models.ImageField('Photo',upload_to='photos',blank=True,default="images/avatar.png")
    salon = models.ForeignKey(Salon)
    jobTitle = models.ForeignKey(JobTitle)
    services = models.ManyToManyField(SalonService)
     
    
    def __unicode__(self):
        return self.str_first_name+" "+self.str_last_name
    

class DiscountType(models.Model):
    DISCOUNT_TYPE = (
        (1, u'Option 1'),
        (2, u'Option 2'),
        (3, u'Option 3'),        
    )
    type=models.IntegerField(_("Type"),max_length=25, choices=DISCOUNT_TYPE,null=True,blank=True)
    static_discount=models.DecimalField(_("Percentage"),null=True, blank=True,max_digits=4, decimal_places=2)
    start_discount=models.DecimalField(_("Start discount"),null=True, blank=True,max_digits=4, decimal_places=2)
    end_discount=models.DecimalField(_("End discount"),null=True, blank=True,max_digits=4, decimal_places=2)
    nb_days=models.IntegerField(_("Number of Days"),null=True, blank=True,)   #number of day 
    nb_months=models.IntegerField(_("Number of Days"),null=True, blank=True,)   #number of day
    stylist = models.ForeignKey(Stylist)
    def __unicode__(self):
        
        if self.type == 1:
            return "Level discount at "+str(self.static_discount)
        else:
            if self.type == 2:
                return "Dutch Auction"
            else:
                return "never discount"
class AdminRole(models.Model):
    name=models.CharField('Name',max_length=50)
    title=models.CharField('title',max_length=50,unique=True)
    permissions = models.ManyToManyField(Permission)
    def __unicode__(self):
        return self.name  


class SalonAdmin(models.Model):

    user=models.ForeignKey(User)
    role=models.ForeignKey(AdminRole)
    salons=models.ManyToManyField("Salon",through='SalonManager',null=True,blank=True)
    def __unicode__(self):
        return self.user.username 
    
class SalonManager(models.Model):
    admin=models.ForeignKey(SalonAdmin)
    salon=models.ForeignKey(Salon)
    def __unicode__(self):
        return self.salon.str_name     
    
 
    


