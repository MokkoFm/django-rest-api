from rest_framework import serializers
from cart.models import Order, Customer, OrderItem, Product, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['quantity', 'product', 'order']


class OrderSerializer(serializers.ModelSerializer):
    #products = OrderItemSerializer(many=True, read_only=True, source=)
    country = serializers.CharField(source="country.title", read_only=True)
    customer_lastname = serializers.CharField(source="customer.lastname")
    customer_firstname = serializers.CharField(source="customer.firstname")
    phonenumber = serializers.CharField(source="customer.phonenumber")
    email = serializers.CharField(source="customer.email")

    class Meta:
        model = Order
        fields = [
            'registrated_at', 'payment_method',
            'customer_lastname', 'customer_firstname',
            'phonenumber', 'email',
            'country', 'order_items'
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


