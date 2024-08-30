from django.contrib import admin
from .models import registertable, vehicleinfo, bookings, contactus , payment


# Register your models here.

class showusers(admin.ModelAdmin):
    list_display = ['name', 'email', 'contactno', 'role']


admin.site.register(registertable, showusers)


class showpayments(admin.ModelAdmin):
    list_display = ["email","card","number","exmonth","exyear","cvv"]

admin.site.register(payment,showpayments)

class showvehicle(admin.ModelAdmin):
    list_display = ['vtype', 'vmodel', 'vnumberplate', 'rateperhour', 'location', 'vphotos']


admin.site.register(vehicleinfo, showvehicle)


class showbookings(admin.ModelAdmin):
    list_display = ['userid','contactno', 'location', 'Message', 'date','bdate', 'vid']


admin.site.register(bookings, showbookings)


class showcontact(admin.ModelAdmin):
    list_display = ['name', 'email', 'number', 'message']


admin.site.register(contactus, showcontact)
