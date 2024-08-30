from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class contactus(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    number = models.BigIntegerField()
    message = models.CharField(max_length=30)


class registertable(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    contactno = models.BigIntegerField()
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class payment(models.Model):
    email = models.ForeignKey(registertable, on_delete=models.CASCADE, null=True)
    card = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    exmonth = models.CharField(max_length=30)
    exyear = models.CharField(max_length=30)
    cvv = models.CharField(max_length=30)


class vehicleinfo(models.Model):
    userid = models.ForeignKey(registertable, on_delete=models.CASCADE, null=True)
    vtype = models.CharField(max_length=30)
    vmodel = models.IntegerField()
    vnumberplate = models.CharField(max_length=20)
    rateperhour = models.IntegerField()
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to="photos")

    def vphotos(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))

    vphotos.allow_tags = True

    def __str__(self):
        return self.vnumberplate


class bookings(models.Model):
    userid = models.ForeignKey(registertable, on_delete=models.CASCADE, null=True)
    contactno = models.BigIntegerField()
    location = models.CharField(max_length=50)
    Message = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    bdate = models.CharField(max_length=20, null=True)
    vid = models.ForeignKey(vehicleinfo, on_delete=models.CASCADE, null=True)
