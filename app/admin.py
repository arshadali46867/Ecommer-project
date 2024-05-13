from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Product)    
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discount_price','description','composition','prodapp','category','product_image']

