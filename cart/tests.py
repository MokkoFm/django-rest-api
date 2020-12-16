from django.test import TestCase
from cart.models import Product, Customer, Country, Order
from cart.models import OrderItem
from decimal import Decimal
import tempfile


class ProductTest(TestCase):
    @classmethod
    def setUpTestData(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        self.product = Product.objects.create(
            title="Pasta",
            description="Pasta, tomatoes, cheese",
            price=20.95,
            image=image
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.product.title, str)
        self.assertIsInstance(self.product.description, str)
        self.assertIsInstance(self.product.price, float)

    def test_max_length_of_title(self):
        product = Product.objects.get(title="Pasta")
        max_length = product._meta.get_field("title").max_length
        self.assertGreaterEqual(max_length, len(product.title))

    def test_max_length_of_description(self):
        product = Product.objects.get(title="Pasta")
        max_length = product._meta.get_field("description").max_length
        self.assertGreaterEqual(max_length, len(product.description))

    def test_float_price_correctly_saves_as_decimal(self):
        product = Product.objects.get(title="Pasta")
        self.assertEqual(product.price, Decimal('20.95'))


class CustomerTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.customer = Customer.objects.create(
            firstname="Sergei",
            lastname="Elsakov",
            phonenumber="+358449494105",
            email="sergei.elsakov91@gmail.com",
            address="Rovaniemi, Kuntotie 5c"
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.customer.firstname, str)
        self.assertIsInstance(self.customer.lastname, str),
        self.assertIsInstance(self.customer.email, str)
        self.assertIsInstance(self.customer.address, str)

    def test_max_length_of_firstname(self):
        customer = Customer.objects.get(firstname="Sergei")
        max_length = customer._meta.get_field("firstname").max_length
        self.assertGreaterEqual(max_length, len(customer.firstname))

    def test_max_length_of_lastname(self):
        customer = Customer.objects.get(lastname="Elsakov")
        max_length = customer._meta.get_field("lastname").max_length
        self.assertGreaterEqual(max_length, len(customer.lastname))

    def test_max_length_of_email(self):
        customer = Customer.objects.get(lastname="Elsakov")
        max_length = customer._meta.get_field("email").max_length
        self.assertGreaterEqual(max_length, len(customer.email))


class CountryTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.country = Country.objects.create(
            title="Finland",
            vat=24.00,
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.country.title, str)
        self.assertIsInstance(self.country.vat, float)

    def test_max_length_of_title(self):
        country = Country.objects.get(title="Finland")
        max_length = country._meta.get_field("title").max_length
        self.assertGreaterEqual(max_length, len(country.title))

    def test_float_vat_correctly_saves_as_decimal(self):
        country = Country.objects.get(title="Finland")
        self.assertEqual(country.vat, Decimal('24.00'))


class OrderTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.customer = Customer.objects.create(
            firstname="Sergei",
            lastname="Elsakov",
            phonenumber="+358449494105",
            email="sergei.elsakov91@gmail.com",
            address="Rovaniemi, Kuntotie 5c"
        )

        self.country = Country.objects.create(
            title="Finland",
            vat=24.00,
        )

        self.order = Order.objects.create(
            registrated_at="2020-12-15T16:53:31+02:00",
            payment_method="Card",
            customer=self.customer,
            country=self.country,
        )

    def test_max_length_of_payment_method(self):
        order = Order.objects.get(customer__lastname="Elsakov")
        max_length = order._meta.get_field("payment_method").max_length
        self.assertGreaterEqual(max_length, len(order.payment_method))


class OrderItemTest(TestCase):
    @classmethod
    def setUpTestData(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name

        self.customer = Customer.objects.create(
            firstname="Sergei",
            lastname="Elsakov",
            phonenumber="+358449494105",
            email="sergei.elsakov91@gmail.com",
            address="Rovaniemi, Kuntotie 5c"
        )

        self.country = Country.objects.create(
            title="Finland",
            vat=24.00,
        )

        self.order = Order.objects.create(
            registrated_at="2020-12-15T16:53:31+02:00",
            payment_method="Card",
            customer=self.customer,
            country=self.country,
        )

        self.product = Product.objects.create(
            title="Pasta",
            description="Pasta, tomatoes, cheese",
            price=20.95,
            image=image
        )

        self.order_item = OrderItem.objects.create(
            product=self.product,
            order=self.order,
            quantity=2,
        )

    def test_min_quantity(self):
        order_item = OrderItem.objects.get(
            order=self.order, product=self.product, quantity=2)
        min_value = 1
        self.assertLessEqual(min_value, order_item.quantity)

    def test_max_quantity(self):
        order_item = OrderItem.objects.get(
            order=self.order, product=self.product, quantity=2)
        max_value = 25
        self.assertGreaterEqual(max_value, order_item.quantity)
