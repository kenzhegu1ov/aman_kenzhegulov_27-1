from django.shortcuts import render, redirect

from posts.constants import PAGINATION_LIMIT
from posts.forms import ProductCreateForm
from posts.models import Products, Review


# Create your views here.


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == "GET":
        products = Products.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page-1):PAGINATION_LIMIT * page]

        if search:
            products = products.filter(
                title__icontains=search) | products.filter(
                description__icontains=search)

            """ starts_with ends_with icontains contains """

        context = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page+1)
        }

        return render(request, 'products/products.html', context=context)


def products_detail_view(request, id):
    if request.method == "GET":
        product = Products.objects.get(id=id)
        review = Review.objects.filter(product_id=id)

        context = {
            'product': product,
            'reviews': review
        }
        return render(request, 'products/detail.html', context=context)


def products_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            Products.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                price=form.cleaned_data.get('price'),
                gpu=form.cleaned_data.get('gpu'),
                cpu=form.cleaned_data.get('cpu'),
                rate=form.cleaned_data.get('rate')
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })


def review_create_view(request, product_id):
    product = Products.objects.get(id=id)

    if request.method == 'POST':
        review_text = request.POST['review_text']
        review = Review(text=review_text, product=product, user=request.user)
        review.save()
        return redirect('detail', product_id=product_id)

    return render(request, 'products/detail.html', {'product': product})
