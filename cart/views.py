from django.shortcuts import render
from cart.models import Product, Customer, Order, OrderItem
from cart.serializers import OrderSerializer, CustomerSerializer
from cart.serializers import OrderItemSerializer, ProductSerializer
from rest_framework import generics
from rest_framework.serializers import ValidationError


def index(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "index.html", context)


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class CustomerCreateView(generics.CreateAPIView):
    serializer_class = CustomerSerializer


class CustomersListView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class OrderItemCreateView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()