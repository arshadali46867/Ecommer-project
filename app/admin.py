from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Product)    
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discount_price','description','composition','prodapp','category','product_image']

@admin.register(CustomerProfileModel)    
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['user','name','locality','city','mobile','zipcode','state']

# @admin.register(CustomerRegistrationModel)    
# class CustomerModelAdmin(admin.ModelAdmin):
#     list_display=['username','email','password1','password2']

