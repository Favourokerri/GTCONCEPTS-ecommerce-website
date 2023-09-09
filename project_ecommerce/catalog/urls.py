from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('products', views.products, name="products"),
]