from django.contrib import admin
from .models import Contact, Menu, Orders, Payment

# Register your models here.
admin.site.register(Contact)
admin.site.register(Menu)
admin.site.register(Orders)
admin.site.register(Payment)