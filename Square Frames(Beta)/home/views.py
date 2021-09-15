from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Testimonial, Order
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

 
# Create your views here.
def index(request):
    return render(request, "index.html")

def mission(request):
    return render(request, "mission.html")

def aboutus(request):
    return render(request, "aboutus.html")

def contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email, subject=subject, message= message, date=datetime.today())
        contact.save()
        messages.success(request, "Message sent!")

        email = EmailMessage(
            'Thanks for purchasing at Square Frames',
            'We will get back to you soon',
            settings.EMAIL_HOST_USER,
            ['email',],
        )
       

    return render(request, "contactus.html")

def testimonials(request):
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            review = request.POST.get("review")
            testimonials = Testimonial(name=name, email=email,review= review, date=datetime.today())
            testimonials.save()
            messages.success(request, "Message sent!")
    
       
        return render(request, "testimonials.html")

def bird(request):
    return render(request, "bird.html")

def landscape(request):
    return render(request, "landscape.html")

def still(request):
    return render(request, "still.html")

def buybird(request):
    return render(request, "buybird.html")

def order(request):
    if request.method == "POST":
        FirstName = request.POST.get("FirstName")
        LastName = request.POST.get("LastName")
        Email = request.POST.get("Email")
        PhoneNumber = request.POST.get("PhoneNumber")
        Address = request.POST.get("Address")
        Country = request.POST.get("Country")
        City = request.POST.get("City")
        State = request.POST.get("State")
        Zip = request.POST.get("Zip")
        PhotoID = request.POST.get("PhotoID")
        order = Order(FirstName=FirstName, LastName=LastName, Email=Email, PhoneNumber=PhoneNumber, Address=Address,
        Country=Country, City=City, State=State, Zip=Zip, PhotoID=PhotoID, date=datetime.today())
        order.save()
       

    return render(request, "order.html")

def portfolio(request):
    return render(request, "portfolio.html")

def specials(request):
    return render(request, "specials.html")

def upload(request):
    return render(request, "upload.html")