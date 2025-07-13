from django.contrib import admin
from .models import Category, Dish

admin.site.register(Category)
admin.site.register(Dish)

from django.contrib import admin
from .models import Booking

admin.site.register(Booking)

from .models import ContactMessage

admin.site.register(ContactMessage)
