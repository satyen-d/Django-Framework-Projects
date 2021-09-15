from django.shortcuts import render, HttpResponse
from datetime import datetime
#from home.models import 
from django.contrib import messages
from home.models import Contact, ClothingOrder, ElectricalOrder, OtherOrder
# Create your views here.
def index(request):
    return render(request, "index.html")

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


def aboutus(request):
    return render(request, "aboutus.html")

def ladies(request):
        if request.method == "POST":
            name = request.POST.get("name")
            phonenumber = request.POST.get("phonenumber")
            style = request.POST.get("style")
            size = request.POST.get("size")
            description = request.POST.get("description")
            ladies = ClothingOrder(name=name, phonenumber=phonenumber, style=style, size= size, description=description, date=datetime.today())
            ladies.save()
            return render(request, "sentcontact.html")


        return render(request, "ladies.html")


def electrical(request):
        if request.method == "POST":
            name = request.POST.get("name")
            phonenumber = request.POST.get("phonenumber")
            product = request.POST.get("product")
            size = request.POST.get("size")
            description = request.POST.get("description")
            electrical = ElectricalOrder(name=name, phonenumber=phonenumber, product=product, size= size, description=description, date=datetime.today())
            electrical.save()
            return render(request, "sentcontact.html")

        return render(request,"electrical.html")

def other(request):
        if request.method == "POST":
            name = request.POST.get("name")
            phonenumber = request.POST.get("phonenumber")
            product = request.POST.get("product")
            size = request.POST.get("size")
            description = request.POST.get("description")
            other = OtherOrder(name=name, phonenumber=phonenumber, product=product, size= size, description=description, date=datetime.today())
            other.save()
            return render(request, "sentcontact.html")

        return render(request,"other.html")
 
