from django.contrib import admin
from cart.models import Product, Customer, Order, OrderItem
# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)