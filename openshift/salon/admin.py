from salon.models import *
from django.contrib import admin

class OpeningHourAdmin(admin.ModelAdmin):
    list_display = ['salon', 'day','open','close','closed']
    list_filter = ['salon']
                  
    

admin.site.register(Salon)
admin.site.register(City)
admin.site.register(Stylist)
admin.site.register(Service)
admin.site.register(SalonService)
admin.site.register(Country)
admin.site.register(JobTitle)
admin.site.register(SalonAdmin)
admin.site.register(AdminRole)
admin.site.register(SalonManager)
admin.site.register(DiscountType)
admin.site.register(OpeningHour,OpeningHourAdmin)