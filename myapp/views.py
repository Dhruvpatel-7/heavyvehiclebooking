from django.shortcuts import render, redirect
from .models import registertable, vehicleinfo, bookings, contactus, payment
from django.contrib import messages


# Create your views here.
def indexpage(request):
    try:
        uid = request.session['logid']
        try:
            checkuser = registertable.objects.get(id=uid)
            num_rows = registertable.objects.count()
            num_row = vehicleinfo.objects.count()
            num_ro = bookings.objects.count()

        except:
            checkuser = None
        owner = False
        if checkuser.role == "Vehicle Owner":
            owner = True
        context = {
            'num_rows': num_rows,
            'num_row': num_row,
            'num_ro': num_ro,
            'checkuser': checkuser,
            'owner': owner,
        }
        return render(request, 'index.html', context)

    except:
        print("except calling")

    return render(request, "index.html")


def servicespage(request):
    try:
        uid = request.session['logid']
        try:
            checkuser = registertable.objects.get(id=uid)

        except:
            checkuser = None
        owner = False
        if checkuser.role == "Vehicle Owner":
            owner = True
        context = {
            'checkuser': checkuser,
            'owner': owner,
        }
        return render(request, "services.html", context)
    except:
        messages.error(request,"LOGIN FIRST")
    return redirect(indexpage)

def payments(request):
    return render(request, "payment.html")

def addpayments(request):
    if request.method == 'POST':
        pcard = request.POST.get("card")
        pnumber = request.POST.get("number")
        pexmonth = request.POST.get("exmonth")
        pexyear = request.POST.get("exyear")
        pcvv = request.POST.get("cvv")
        uid = request.session['logid']
        getcarddetails = payment.objects.get()
        print(getcarddetails.card)
        gcard=getcarddetails.card
        gnumber=getcarddetails.number
        gmonth=getcarddetails.exmonth
        gyear=getcarddetails.exyear
        gcvv=getcarddetails.cvv
        if gcard == pcard and gnumber==pnumber and gmonth==pexmonth and gyear==pexyear and gcvv==pcvv:
            # print("payment accepted")
            messages.success(request, "payment successfull")
        else:
            messages.error(request, "re enter details")

        return redirect(payments)
    else:
        pass
    return redirect(payments)


def checkout(request, id):
    getdata = vehicleinfo.objects.get(id=id)
    context = {
        'data': getdata
    }

    return render(request, "checkout.html", context)


def contactpage(request):
    try:
        uid = request.session['logid']
        try:
            checkuser = registertable.objects.get(id=uid)

        except:
            checkuser = None
        owner = False
        if checkuser.role == "Vehicle Owner":
            owner = True
        context = {
            'checkuser': checkuser,
            'owner': owner,
        }
        return render(request, "contact.html", context)
    except:
        messages.error(request,"LOGIN FIRST")
    return redirect(indexpage)

def vehiclespage(request):
    try:
        uid = request.session['logid']
        fetchvehicle = vehicleinfo.objects.all()

        try:
            checkuser = registertable.objects.get(id=uid)

        except:
            checkuser = None
        owner = False
        if checkuser.role == "Vehicle Owner":
            owner = True

        context = {
            'data': fetchvehicle,
            'checkuser': checkuser,
            'owner': owner,
        }
        return render(request, "vehicles.html", context)
    except:
        messages.error(request,"LOGIN FIRST")
    return redirect(indexpage)



def clientpage(request):
    uid = request.session['logid']
    getdata = registertable.objects.get(id=uid)
    context = {
        'data': getdata
    }
    return render(request, "clientsite.html", context)


def ownerpage(request):
    uid = request.session['logid']
    myvehicle = vehicleinfo.objects.filter(userid=uid)
    getdata = registertable.objects.get(id=uid)
    context = {
        'details': myvehicle,
        'data': getdata
    }
    return render(request, "ownersite.html", context)


def adddata(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        contactno = request.POST.get("contactno")
        role = request.POST.get("role")
        try:
            checkusers = registertable.objects.get(email=email)

        except:
            checkusers = None

        if checkusers is not None:
            messages.error(request, "email already exist")

        else:
            insertdata = registertable(name=name, email=email, password=password, contactno=contactno, role=role)
            insertdata.save()
            messages.success(request, "Register successfully")


    else:
        pass
    return render(request, "index.html")


def checklogindata(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            checkuser = registertable.objects.get(email=email, password=password)
            request.session['logid'] = checkuser.id
            request.session['logname'] = checkuser.name
            request.session['logrole'] = checkuser.role
            request.session.save()
        except:
            checkuser = None

        if checkuser is not None:
            if checkuser.role == "Vehicle Owner":
                messages.success(request, "Login successfully")
                return redirect(indexpage)
        else:
            messages.success(request, "Email and Password incorrect")
            return render(request, "index.html")
    return render(request, "index.html")


def adddatacontact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("message")
        try:
            checkusers = contactus.objects.get(email=email)

        except:
            checkusers = None

        if checkusers is not None:
            messages.error(request, "Your Request Is Already Registered")

        else:
            insertdata = contactus(name=name, email=email, number=number, message=message)
            insertdata.save()
            messages.success(request, "Request Sent successfully")


    else:
        pass
    return render(request, "contact.html")


def updatedetails(request, id):
    uid = request.session['logid']
    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    contactno = request.POST.get("contactno")

    getdata = registertable.objects.get(id=uid)
    getdata.name = name
    getdata.email = email
    getdata.password = password
    getdata.contactno = contactno
    getdata.save()
    messages.success(request, "Profile edit successfully")
    return render(request, "index.html")


def addvehicle(request):
    if request.method == 'POST':
        vtype = request.POST.get("vtype")
        vmodel = request.POST.get("vmodel")
        vnumberplate = request.POST.get("vnumberplate")
        rateperhour = request.POST.get("rateperhour")
        location = request.POST.get("location")
        image = request.FILES["image"]
        uid = request.session['logid']
        try:
            checkusers = vehicleinfo.objects.get(vnumberplate=vnumberplate)

        except:
            checkusers = None

        if checkusers is not None:
            messages.error(request, "NumberPlate already Registered")

        else:
            insertdata = vehicleinfo(userid=registertable(id=uid), vtype=vtype, vmodel=vmodel,
                                     vnumberplate=vnumberplate, rateperhour=rateperhour,
                                     location=location, image=image)
            insertdata.save()
            messages.success(request, "Vehicle Added successfully")

    else:
        pass
    return redirect(ownerpage)


def bookdata(request, id):
    if request.method == 'POST':
        contactno = request.POST.get("contactno")
        location = request.POST.get("location")
        message = request.POST.get("message")
        bdate = request.POST.get("bdate")
        uid = request.session['logid']

        if contactno and location and message and bdate == '':
            messages.error(request, "Fill all fields")

        else:
            vid = id
            addata = bookings(userid=registertable(id=uid), contactno=contactno, location=location, Message=message,
                              bdate=bdate, vid=vehicleinfo(id=vid))
            addata.save()
            return redirect(payments)
            pass
        return render(request, 'vehicles.html')
    else:
        pass
    return render(request, 'vehicles.html')


def editvehicle(request, id):
    getdata = vehicleinfo.objects.get(id=id)
    context = {
        'data': getdata
    }

    return render(request, "editvehicle.html", context)


def delete(request, id):
    fetchdata = vehicleinfo.objects.get(id=id)
    fetchdata.delete()
    return redirect(ownerpage)


def bookingpage(request):

    uid = request.session['logid']
    try:
        checkuser = registertable.objects.get(id=uid)

    except:
        checkuser = None
    print(checkuser.role)
    if checkuser.role == "Vehicle Owner":
        data = bookings.objects.filter(userid=uid)

        user = registertable.objects.get(id=uid)

        try:
            myvehdet = vehicleinfo.objects.filter(userid=user)
        except vehicleinfo.DoesNotExist:
            myvehdet = None

        mybookings = bookings.objects.filter(vid__in=myvehdet)

        context = {
            'data': data,
            'mybookings': mybookings,
        }
        return render(request, "booking.html", context)
    else:
        mybookings = bookings.objects.filter(userid=uid)
        context = {
            'mybookings': mybookings
        }
    return render(request, "booking.html",context)


def logout(request):
    try:
        del request.session["logid"]
        del request.session["logname"]
        del request.session['logrole']

    except:
        pass
    return render(request, "index.html")


def forgotpass(request):
    return render(request, "forgotpass.html")


def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST['email']
        try:
            user = registertable.objects.get(email=username)

        except registertable.DoesNotExist:
            user = None
        # if user exist then only below condition will run otherwise it will give error as described in else condition.
        if user is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  # we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################

            msg = "hello here it is your new password  " + password  # this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                'krushanuinfolabz@gmail.com',
                [username],
                fail_silently=False,
            )

            # NOTE: must include below details in settings.py
            # detail tutorial - https://www.geeksforgeeks.org/setup-sending-email-in-django-project/
            # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            # EMAIL_HOST = 'smtp.gmail.com'
            # EMAIL_USE_TLS = True
            # EMAIL_PORT = 587
            # EMAIL_HOST_USER = 'mail from which email will be sent'
            # EMAIL_HOST_PASSWORD = 'pjobvjckluqrtpkl'   #turn on 2 step verification and then generate app password which will be 16 digit code and past it here

            #############################################

            # now update the password in model
            cuser = registertable.objects.get(email=username)
            cuser.password = password
            cuser.save(update_fields=['password'])

            print('Mail sent')
            messages.info(request, 'mail is sent')
            return redirect(indexpage)

        else:
            messages.info(request, 'This account does not exist')
    return redirect(indexpage)

def cancelbook(request, id):
    fetchdata = bookings.objects.get(id=id)
    fetchdata.delete()
    return render(request, "booking.html")

