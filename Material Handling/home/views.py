from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from datetime import datetime

from django.contrib import messages
from home.models import Contact, Shop, Transport, Order
# Create your views here.

def user_login(request):
    content = {}
    if request.method == "POST":
        pass
    else:
        return render(request, "auth/login.html", content)


def success(request):
    pass

def user_logout(request):
    pass

@login_required
def index(request):
    stud = Shop.objects.all().order_by("-id")
    return render(request, "index.html", {"stu": stud})

def Pune(request):
    stud = Shop.objects.filter(city = "Pune")
    return render(request, "pune.html", {"stu": stud})

def Roha(request):
    stud = Shop.objects.filter(city = "Roha")
    return render(request, "roha.html", {"stu": stud})

def Mumbai(request):
    stud = Shop.objects.filter(city = "Mumbai")
    return render(request, "mumbai.html", {"stu": stud})

def Punetrans(request):
    stud = Transport.objects.filter(city = "Pune")
    return render(request, "punetrans.html", {"stu": stud})

def Rohatrans(request):
    stud = Transport.objects.filter(city = "Roha")
    return render(request, "rohatrans.html", {"stu": stud})

def Mumbaitrans(request):
    stud = Transport.objects.filter(city = "Mumbai")
    return render(request, "mumbaitrans.html", {"stu": stud})

def registerview(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form":form})


def shopregistration(request):
    return render(request, "Shopreg.html")

def Transports(request):
    stud = Order.objects.all()
    return render(request, "transport.html", {"stu": stud})

def Pay(request):
    return render(request, "ptmpay.html")

def transregistration(request):
    return render(request, "Transreg.html")

def materials(request):
    return render(request, "materials.html")


def contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email, subject=subject, message= message, date=datetime.today())
        contact.save()
        return render(request, "sentcontact.html")
    return render(request, "contactus.html")
    

def shoperg(request):
    if request.method == "POST":
        name = request.POST.get("name")
        sname = request.POST.get("sname")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        email = request.POST.get("email")
        shop_details = request.POST.get("shop_details")
        shop = Shop(name=name, sname=sname, phone=phone,city=city, email=email, shop_details=shop_details, date=datetime.today())
        shop.save()
        return render(request, "sentcontact.html")


def order(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        add1 = request.POST.get("add1")
        add2 = request.POST.get("add2")
        shop = Order(name=name, email=email, phone=phone,city=city, add1=add1,add2=add2, date=datetime.today())
        shop.save()
        return render(request, "paytrans.html")
    return render(request, "paytrans.html")
    


def transrg(request):
    if request.method == "POST":
        name = request.POST.get("name")
        sname = request.POST.get("sname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        city = request.POST.get("city")
        transport_details = request.POST.get("transport_details")
        transport = Transport(name=name, sname=sname, phone=phone, email=email,city=city, transport_details=transport_details, date=datetime.today())
        transport.save()
        return render(request, "sentcontact.html")

def authen(request):

        #username = request.POST.get('uname')
        #fname = request.POST.get('fname')
        #lname = request.POST.get('lname')
       # email = request.POST.get('email')
       # phn = request.POST.get('phn')
       # pass1 = request.POST.get('pass1')
       # pass2 = request.POST.get('pass2')

       # myuser = User(username = username, password = pass1, email = email)
       # myuser.first_name = fname
       # myuser.last_name = lname
       # myuser.save()
        messages.success(request, "Your Material Handling account is succssfully created!")
        return render(request, "authen.html")
        #, {"form":form}
    