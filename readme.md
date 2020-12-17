# Qvantel - trial work to implement API

Frontent will be implemented by [link](https://cart-rest-api.herokuapp.com/).

## Installation

Python 3 must be installed. Download the code.

### Environment Variables 

Some of settings are taken from environment variables. Create `.env` near `manage.py` and write 2 variables there in this format:`VARIABLE=value`.

- `SECRET_KEY=your secret key`
- `DEBUG=True or False` - (default:`True`) debug mode. Set `False` for production.  
- `DB_NAME=name` 
- `DB_USER=user` 
- `DB_PASSWORD=password` 
- `DB_HOST=host` 

### Requirements

Install requirements with command:
```
pip install -r requirements.txt
```

## Running Code

Create database with command:
```
python manage.py migrate
```

Run development server with command:
```
python manage.py runserver
```

## Permissions 
For using API you should be authenticated. You can use test superuser:
- `LOGIN - qvantel` 
- `PASSWORD - 12345678` 

## Admin panel 

Create superuser with command:
```
python manage.py createsuperuser
```

Link to the admin panel: `http://127.0.0.1:8000/admin/`. 

## Using Browsable API

You can use browsable API to work with models.

How to work with `Product`:
- [Create product](https://cart-rest-api.herokuapp.com/api/product/create)
- [List of products](https://cart-rest-api.herokuapp.com/api/products)
- [Get product-detail](https://cart-rest-api.herokuapp.com/api/product-detail/1) 

How to work with `Customer`:
- [Create customer](https://cart-rest-api.herokuapp.com/api/customer/create) 
- [List of customers](https://cart-rest-api.herokuapp.com/api/customers) 
- [Get customer-detail](https://cart-rest-api.herokuapp.com/api/customer-detail/1) 

How to work with `Country`:
- [Create country](https://cart-rest-api.herokuapp.com/api/country/create) 
- [List of countries](https://cart-rest-api.herokuapp.com/api/countries) 
- [Get country-detail](https://cart-rest-api.herokuapp.com/api/country-detail/1) 

How to work with `Order`:
- [Create order](https://cart-rest-api.herokuapp.com/api/order/create) 
- [List of orders](https://cart-rest-api.herokuapp.com/api/orders) 
- [Get order-detail](https://cart-rest-api.herokuapp.com/api/order-detail/1) 

How to work with `Order-item`:
- [Create order-item](https://cart-rest-api.herokuapp.com/api/order-item/create) 
- [List of order-items](https://cart-rest-api.herokuapp.com/api/order-items) 

## Project's Purposes

The code was written as a trial task for Qvantel.
