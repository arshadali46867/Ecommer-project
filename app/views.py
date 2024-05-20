from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from django.db.models import Count
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from .forms import CustomerRegistrationForm

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


class CustomerRegistration(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render (request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form .is_valid():
            form.save()
            messages.success(request,"Congratulation! User Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")

        return render(request,'app/customerregistration.html',{'form':form})    





def login(request):
    
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            # cd=form.cleaned_data
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                # if user.is_active:
                   auth_login(request,user)
                   return render(request,'app/home.html')
                # else:
                #     return render(request,'app/customerregistration.html')
                

            else:
                return HttpResponse('invalid login')    

                
    else:
        form=LoginForm()
        return render(request,'app/login.html',{'form':form})


class ProfileView(View):
    def get(self,request) :
        form=CustomerProfileForm()
        return render (request,'app/profile.html',{'form':form}) 
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
           
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg=CustomerProfileModel(user=user,name=name,locality=locality,city=city,mobile=mobile,zipcode=zipcode)

            reg.save()
            messages.success(request,'Congratulations! Profile Save Scuccesssfully')




        return render (request,'app/profile.html',{'form':form}) 


# class ProfileView(View):
#     def get(self, request):
#         form = CustomerProfileForm()
#         return render(request, 'app/profile.html', {'form': form})

#     def post(self, request):
#         form = CustomerProfileForm(request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)  # Do not save yet
#             profile.user = request.user  # Set the user field
#             profile.save()  # Now save the profile instance
#             messages.success(request, 'Congratulations! Profile saved successfully')
#             return redirect('profile')  # Redirect after successful save to avoid resubmission
#         return render(request, 'app/profile.html', {'form': form})



def AddressView(request):
    add=CustomerProfileModel.objects.filter(user=request.user)
    return render(request,'app/address.html',locals())




class UpdateAddress(View):
    def get(self,request,pk):
        add=CustomerProfileModel.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request,'app/updateaddress.html',locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add=CustomerProfileModel.objects.get(pk=pk)

            add.user=request.user
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.city=form.cleaned_data['city']
            add.mobile=form.cleaned_data['mobile']
            add.state=form.cleaned_data['state']
            add.zipcode=form.cleaned_data['zipcode']

            add.save()
            messages.success(request,'Congratulations! Update Scuccesssfully')
        else:
            messages.success(request,'InvalidInput Data')
        
        return redirect('address')
        # return render(request,'app/updateaddress.html',locals())
