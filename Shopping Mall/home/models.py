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

class ClothingOrder(models.Model):
    name = models.CharField(max_length=122)
    phonenumber = models.CharField(max_length=122)
    style = models.CharField(max_length=500)
    size = models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class ElectricalOrder(models.Model):
    name = models.CharField(max_length=122)
    phonenumber = models.CharField(max_length=122)
    product = models.CharField(max_length=500)
    size = models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class OtherOrder(models.Model):
    name = models.CharField(max_length=122)
    phonenumber = models.CharField(max_length=122)
    product = models.CharField(max_length=500)
    size = models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name