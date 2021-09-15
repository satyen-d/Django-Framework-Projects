from django.contrib import admin
from home.models import Contact, ClothingOrder, ElectricalOrder, OtherOrder
# Register your models here.
admin.site.register(Contact)
admin.site.register(ClothingOrder)
admin.site.register(ElectricalOrder)
admin.site.register(OtherOrder) 