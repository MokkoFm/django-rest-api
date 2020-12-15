from django.contrib import admin
from cart.models import Product, Customer, Order, OrderItem, Country
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]


admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(Country)
