from django.urls import path
from cart.views import OrderCreateView, OrderListView, OrderDetailView
from cart.views import CustomerCreateView, CustomerDetailView, CustomersListView
from cart.views import OrderItemCreateView, OrderItemListView
from cart.views import ProductCreateView, ProductDetailView, ProductsListView
from cart.views import CountryCreateView, CountriesListView, CountryDetailView

app_name = "cart"

urlpatterns = [
    path('order/create', OrderCreateView.as_view()),
    path('order-detail/<int:pk>', OrderDetailView.as_view()),
    path('orders', OrderListView.as_view()),
    path('customer/create', CustomerCreateView.as_view()),
    path('customer-detail/<int:pk>', CustomerDetailView.as_view()),
    path('customers', CustomersListView.as_view()),
    path('order-item/create', OrderItemCreateView.as_view()),
    path('order-items', OrderItemListView.as_view()),
    path('product/create', ProductCreateView.as_view()),
    path('products', ProductsListView.as_view()),
    path('product-detail/<int:pk>', ProductDetailView.as_view()),
    path('country/create', CountryCreateView.as_view()),
    path('countries', CountriesListView.as_view()),
    path('country-detail/<int:pk>', CountryDetailView.as_view())
]
