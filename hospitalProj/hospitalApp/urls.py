from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('new', views.newCustomer, name='newCustomer'),
    path('read', views.getAllCustomers, name='getAllCustomers'),
    path('read/<int:id>', views.getOneCustomer, name='getOneCustomer'),
    path('update/<int:id>', views.updateCustomer, name='updateCustomer'),
    path('delete/<int:id>', views.deleteCustomer, name='deleteCustomer'),
    path('account/new', views.newAccount, name='newAccount'),
    path('account/update/<int:id>', views.updateAccount, name='updateAccount'),
    path('account/delete/<int:id>', views.deleteAccount, name='deleteAccount'),
]