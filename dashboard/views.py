from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm,OrderForm
from django.contrib import messages

from .models import Order, Product ,Category 
# Create your views here.
@login_required(login_url='user-login')
def index(request):
    order = Order.objects.all()
    product = Product.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    return render(request,'dashboard/index.html',{'order':order, 'form': form,'product':product})

# @login_required(login_url='user-login')
# def products(request):
#     return render(request,'dashboard/products.html',{})

@login_required(login_url='user-login')
def customers(request):
    return render(request,'dashboard/staff.html',{})

@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
def customers(request):
    customer = User.objects.all()
    
    context = {
        'customer': customer,
   
    }
    return render(request, 'dashboard/customers.html', context)



@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
def customer_detail(request, pk):
 
    customers = User.objects.get(id=pk)
    context = {
        'customers': customers,
       
    }
    return render(request, 'dashboard/customers_detail.html', context)




@login_required(login_url='user-login')
def products(request):
    product = Product.objects.all()
   

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            
            return redirect('dashboard-products')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form,
     
    }
    return render(request, 'dashboard/products.html', context)


@login_required(login_url='user-login')
def product_detail(request, pk):
    context = {

    }
    return render(request, 'dashboard/products_detail.html', context)




@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/products_edit.html', context)


@login_required(login_url='user-login')
# @allowed_users(allowed_roles=['Admin'])
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)



@login_required(login_url='user-login')
def order(request):
    order = Order.objects.all()

    context = {
        'order': order,
  
    }
    return render(request, 'dashboard/order.html', context)