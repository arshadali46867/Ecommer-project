

from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.home),
    path('about',views.About,name='about'),
    path('contant',views.Contact,name='contact'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('product-detail/<int:pk>',views.ProductDetails.as_view(),name='product-detail')
]
