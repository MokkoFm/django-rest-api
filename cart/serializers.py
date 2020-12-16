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


class OrderItemListSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source="product.title", read_only=True)
    price = serializers.DecimalField(
        source="product.price", read_only=True,
        max_digits=8, decimal_places=2)

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price', 'total']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    order_items = OrderItemListSerializer(many=True, read_only=True)
    country = serializers.CharField(source="country.title", read_only=True)
    customer_lastname = serializers.CharField(source="customer.lastname")
    customer_firstname = serializers.CharField(source="customer.firstname")
    phonenumber = serializers.CharField(source="customer.phonenumber")
    email = serializers.CharField(source="customer.email")

    class Meta:
        model = Order
        fields = [
            'id', 'registrated_at', 'payment_method',
            'customer_lastname', 'customer_firstname',
            'phonenumber', 'email', 'country',
            'order_items', 'cart_total', 'cart_items_amount',
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
