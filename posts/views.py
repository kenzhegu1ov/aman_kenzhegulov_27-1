from django.shortcuts import render
from posts.models import Products


# Create your views here.


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == "GET":
        products = Products.objects.all()
        context = {
            'products': products
        }

        return render(request, 'products/products.html', context=context)


def post_detail_view(request, id):
    if request.method == "GET":
        product = Products.objects.get(id=id)

        context = {
            'product': product
        }
        return render(request, 'products/detail.html', context=context)
