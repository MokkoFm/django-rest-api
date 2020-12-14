from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def register_order(request):
    return render(request)


def product_list_api(request):
    return render(request)