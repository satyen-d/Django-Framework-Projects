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

class Shop(models.Model):
    name = models.CharField(max_length=122)
    sname = models.CharField(max_length=500)
    phone = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    shop_details = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    add1 = models.TextField()
    add2 = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Transport(models.Model):
    name = models.CharField(max_length=122)
    sname = models.CharField(max_length=500)
    phone = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    transport_details = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
