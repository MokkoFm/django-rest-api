from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class Product(models.Model):
    title = models.CharField(verbose_name='title', max_length=50)
    description = models.TextField(verbose_name='description', blank=True)
    price = models.DecimalField(
        verbose_name='price', max_digits=8, decimal_places=2)
    image = models.ImageField(
        upload_to="images", verbose_name="image of product")

    def __str__(self):
        return self.title

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @property
    def image_url(self):
        try:
            url = self.image.url
        except AttributeError:
            url = ''
        return url

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"


class Customer(models.Model):
    firstname = models.CharField(max_length=50, verbose_name="firstname")
    lastname = models.CharField(max_length=50, verbose_name="lastname")
    phonenumber = PhoneNumberField(blank=True, verbose_name="phonenumber")
    email = models.EmailField(
        max_length=100, blank=True, verbose_name="e-mail")
    address = models.TextField(verbose_name="address", null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        verbose_name = "customer"
        verbose_name_plural = "customers"


class Country(models.Model):
    title = models.CharField(max_length=50, verbose_name="country")
    vat = models.DecimalField(
        verbose_name='vat', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"


class Order(models.Model):
    PAYMENT_METHOD = [
        ('Cash', 'By cash'),
        ('Card', 'By card'),
    ]

    registrated_at = models.DateTimeField(
        default=timezone.now, verbose_name='data of registration')
    payment_method = models.CharField(
        max_length=4, choices=PAYMENT_METHOD,
        default='Card', verbose_name='payment method')
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE,
        related_name='orders', verbose_name='customer of order', null=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="orders", null=True,
        verbose_name="country of order")

    def __str__(self):
        return f" Order number - {self.id}"

    @property
    def cart_total(self):
        return sum([item.total for item in self.order_items.all()])

    @property
    def cart_items_amount(self):
        return sum([item.quantity for item in self.order_items.all()])

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='product_items')
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,
        related_name='order_items')
    quantity = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(25)],
        verbose_name='quantity', default=0)

    def __str__(self):
        return f"{self.product}: {self.quantity}"

    @property
    def total(self):
        return self.product.price * self.quantity

    class Meta:
        verbose_name = "order item"
        verbose_name_plural = "order items"
