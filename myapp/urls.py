from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage, name="index.html"),
    path('servicespage', views.servicespage, name="services.html"),
    path('contactpage', views.contactpage, name="contact.html"),
    path('checkout/<int:id>', views.checkout, name="checkout.html"),
    path('vehiclespage', views.vehiclespage, name="vehicles.html"),
    path('ownerpage', views.ownerpage, name="ownersite.html"),
    path('editvehicle/<int:id>', views.editvehicle, name="editvehicle.html"),
    path('clientpage', views.clientpage, name="clientsite.html"),
    path('adddata', views.adddata, name="adddata"),
    path('logout', views.logout, name="logout"),
    path('addvehicle', views.addvehicle, name="addvehicle"),
    path('forgotpass', views.forgotpass, name="forgotpass"),
    path('bookingpage', views.bookingpage, name="bookingpage"),
    path('payments', views.payments, name="payments"),
    path('addpayment', views.addpayments, name="addpayment"),

    path('forgotpassword', views.forgotpassword, name="forgotpassword"),
    path('adddatacontact', views.adddatacontact, name="adddatacontact"),
    path('checklogindata', views.checklogindata, name="checklogindata"),
    path('updatedetails/<int:id>', views.updatedetails,name="updatedetails"),
    path('bookdata/<int:id>', views.bookdata,name="bookdata"),
    path('cancelbook/<int:id>', views.cancelbook,name="cancelbook"),
]