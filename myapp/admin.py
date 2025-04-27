from django.contrib import admin
from .models import *
# Register your models here.
class showregister(admin.ModelAdmin):
    list_display = ['name','email','phone','password','address','gender','role','profile_photo']
admin.site.register(registermodel,showregister)

class showCategory(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Category,showCategory)

class showProduct(admin.ModelAdmin):
    list_display = ['name','category','image_photo','price','description','status','seller']
admin.site.register(Product,showProduct)

class showproductimage(admin.ModelAdmin):
    list_display = ['productid','p_photo']
admin.site.register(productimage,showproductimage)

class showcart(admin.ModelAdmin):
    list_display = ["id","userid","productid","quantity","totalamount","orderstatus","orderid"]

admin.site.register(cart,showcart)

class showorder(admin.ModelAdmin):
    list_display = ["id","userid","finaltotal","phone","address","paymode","status"]

admin.site.register(ordermodel,showorder)