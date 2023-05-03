from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Products, Review
from posts.forms import ProductCreateForm, ReviewCreateForm


# Create your views here.


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == "GET":
        products = Products.objects.all()
        search = request.GET.get('search')

        if search:
            products = products.filter(
                title__icontains=search) | products.filter(
                description__icontains=search)

            """ starts_with ends_with icontains contains """

        context = {
            'products': products,
            'user': request.user
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