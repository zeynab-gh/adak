from django.contrib import admin

from .import models
from .models import Category,Customer,Order,Product,Profile

from django.contrib.auth.models import User



admin.site.register(models.Customer)

admin.site.register(models.Category)

admin.site.register(models.Order)

admin.site.register(models.Product)
admin.site.register(models.Profile)


class ProfileInine(admin.StackedInline):
    model = models.Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields =['username','first_name','last_name','email']
    inlines = [ProfileInine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)