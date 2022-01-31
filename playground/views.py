from django.shortcuts import render
from store.models import Product, Customer, Collection, Cart, CartItem

def say_hello(request):
  pass
  
  
  


  
  return render(request, 'hello.html', { 'name': 'Hello, Brendon!' })