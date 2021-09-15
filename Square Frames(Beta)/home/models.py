from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=500)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    review = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Order(models.Model):
    FirstName = models.CharField(max_length=122)
    LastName = models.CharField(max_length=122)
    Email = models.CharField(max_length=122)
    PhoneNumber= models.CharField(max_length=122)
    Address = models.TextField()
    Country = models.CharField(max_length=122)
    City = models.CharField(max_length=122)
    State = models.CharField(max_length=122)
    Zip = models.CharField(max_length=122)
    PhotoID = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.FirstName
