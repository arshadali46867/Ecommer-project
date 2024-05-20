from django.urls import path

from django.contrib.auth import views as auth_views
from .forms import MyPasswordChangeForm,MySetPasswordForm
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('',views.home),
    path('about',views.About,name='about'),
    path('contant',views.Contact,name='contact'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('product-detail/<int:pk>',views.ProductDetails.as_view(),name='product-detail'),
    path('customerregistration',views.CustomerRegistration.as_view(),name='customerregistration'),
    path('login',views.login,name='login'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address',views.AddressView,name='address'),
    path('updateaddress/<int:pk>',views.UpdateAddress.as_view(),name='updateaddress'),


    # reset password

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='app/registration/password_reset_form.html'),name='password_reset'),
    path('password/reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/registration/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='app/registration/password_reset_complete.html'),name='password_reset_complete'),

# passwordchange

      path('passwordchange',auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
      path('passwordchangedone',auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),


]
