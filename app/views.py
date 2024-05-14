from django.shortcuts import render 
from django.http import HttpResponse
from django.views import View
from .models import *
from django.db.models import Count

# Create your views here.


def home(request):
    return render (request ,'app/home.html')

def About(request):
    return render (request ,'app/about.html')

def Contact(request):
    return render (request ,'app/contact.html')



class CategoryView(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request,'app/category.html',locals())
    


class ProductDetails(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,'app/productdetails.html',locals())
    
