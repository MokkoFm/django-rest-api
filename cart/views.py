from django.shortcuts import render
from cart.models import Product, Customer, Order, OrderItem
from cart.serializers import OrderSerializer, OrderListSerializer
from cart.serializers import CustomerSerializer, ProductSerializer
from cart.serializers import OrderItemSerializer, OrderItemListSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser


def index(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "index.html", context)


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


class OrderListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


class CustomerCreateView(generics.CreateAPIView):
    serializer_class = CustomerSerializer


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomersListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class OrderItemCreateView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer


class OrderItemListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderItemListSerializer
    queryset = OrderItem.objects.all()


class ProductCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer


class ProductsListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
