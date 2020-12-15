from django.urls import path
from cart.views import OrderCreateView, CustomerCreateView, CustomerDetailView
from cart.views import OrderItemCreateView, OrderListView, OrderItemListView
from cart.views import ProductCreateView, ProductDetailView
from cart.views import ProductsListView, CustomersListView

app_name = "cart"

urlpatterns = [
    path('order/create', OrderCreateView.as_view()),
    path('customer/create', CustomerCreateView.as_view()),
    path('customer-detail/<int:pk>', CustomerDetailView.as_view()),
    path('customers', CustomersListView.as_view()),
    path('order-item/create', OrderItemCreateView.as_view()),
    path('order-items', OrderItemListView.as_view()),
    path('orders', OrderListView.as_view()),
    path('product/create', ProductCreateView.as_view()),
    path('products', ProductsListView.as_view()),
    path('product-detail/<int:pk>', ProductDetailView.as_view())
]
