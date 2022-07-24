#categories/models.py
import email
from itertools import product
from operator import mod, truediv
from django.db import models

#class Categories(models.Model):
 #   name = models.CharField(max_length=200)
  #  description = models.TextField()

   # def __str__(self):
    #    return self.name

from django.contrib.auth.models import User




class Product(models.Model):
    name = models.CharField(max_length=200)
    P_TYPE_CHOICES= [
    ('SW', 'Software'),
    ('HW', 'Hardware'),
    ]
    p_type = models.CharField(
        max_length=2,
        choices=P_TYPE_CHOICES,
        default= '',
null=False, blank=False 
	
    )
    
    m_price = models.FloatField()
    available = models.BooleanField(default=False, null=True, blank = True)
    image = models.ImageField(null=True, blank=False)
    description = models.TextField(default = False, max_length=800)
    rent_price = models.FloatField(default=False)
    deposit = models.FloatField(default=False)

    def __str__(self):
        return str(self.name)

    @property

    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url







#class Inventory():



#class Rent():


class Order(models.Model):
   # customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    #image
    def __str__(self):
        return str(self.user)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null= True, blank= True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.rent_price * self.quantity
        return total
    def __str__(self):
        return str(self.order)


class Payment(models.Model):
    #customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)
    transaction_amt = models.FloatField(null=True)
    pay_date = models.DateTimeField(auto_now=True)
    pay_status = models.BooleanField(default=False,null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    
    






#class Refund():


#class feedback():


