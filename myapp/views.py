
from django.http import JsonResponse
from multiprocessing import context
from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth import login,authenticate
from .models import *
from django.contrib import messages
import json

# Create your views here.
def home(request):
    return render(request, 'home.html')

def aboutuspage(request):
    return render(request, 'about.html')

def servicepage(request):
    return render(request, 'services.html')

def product(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'products.html', context)
    
def products_HW(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'products_HW.html', context)

def products_SW(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'products_SW.html', context)

def cart(request):

    if request.user.is_authenticated:
        myuser = request.user
        order, created = Order.objects.get_or_create(user=myuser, complete =False)
        
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cat_total':0, 'get_cart_items':0}

    #items = OrderItem.objects.all()
    context = {'items':items, 'order':order}
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        myuser = request.user
        order, created = Order.objects.get_or_create(user=myuser, complete =False)
        
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cat_total':0, 'get_cart_items':0}

    #items = OrderItem.objects.all()
    context = {'items':items, 'order':order}
    return render(request, 'checkout.html', context)

def renting(request):
    return render(request, 'renting.html')

def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=pwd)
            login(request,user)
            
    form=SignupForm
    return render(request, 'registration/signup.html',{'form':form})

def updateItem(request):
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']
    
    print('Action:', action)
    print('productId:', productId)

    myuser = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=myuser, complete =False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product) 

    return JsonResponse('Item was added', safe=False)