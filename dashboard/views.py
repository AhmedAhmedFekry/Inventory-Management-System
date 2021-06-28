from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'dashboard/index.html',{})

def products(request):
    return render(request,'dashboard/products.html',{})

def customers(request):
    return render(request,'dashboard/staff.html',{})
def order(request):
   
    return render(request, 'dashboard/order.html', {})