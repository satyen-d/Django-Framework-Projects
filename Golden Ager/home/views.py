from django.shortcuts import render
from home.models import Contact
from django.contrib import messages
from datetime import datetime
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
        messages.success(request, "Contact form submitted, our team will be in touch with you shortly!")

    return render(request,"contactus.html")

def dietplan(request):
    if request.method == "POST":
        age = request.POST.get("age")
        if 39<abs(int(age))<51:
            return render(request, "age40.html")
        if 50<abs(int(age))<61:
            return render(request, "age50.html")
        if 60<abs(int(age))<71:
            return render(request, "age60.html")        
        if 70<abs(int(age))<81:
            return render(request, "age70.html")        
        if 80<abs(int(age)):
            return render(request, "age80.html")        
    return render(request, "index.html") 