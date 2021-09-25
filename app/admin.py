from django.contrib import admin
from app.models import User, Beer, Order
# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass
# @admin.register(Beer)
# class BeerAdmin(admin.ModelAdmin):
#     pass
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     pass

admin.site.register(User)
admin.site.register(Beer)
admin.site.register(Order)