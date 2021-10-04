from django.shortcuts import render, get_object_or_404, redirect
from .models import Products, Categories
from .forms import ProductsForm

# Create your views here.

def index(request):
    products = Products.objects.all()
    context = {
        'products': products,
        'title': 'Список товаров',
    }
    return render(request=request, template_name='products/index.html', context=context)

def get_category(request, category_id):
    products = Products.objects.filter(category_id=category_id)
    category = Categories.objects.get(pk=category_id)
    context = {
        'products': products,
        'category': category,
    }
    return render(request=request, template_name='products/category.html', context=context)

def view_product(request, product_id):
    # product = Products.objects.get(pk=product_id)
    product = get_object_or_404(klass=Products, pk=product_id)
    context = {
        'product': product,
    }
    return render(request=request, template_name='products/view_product.html', context=context)

def add_product(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            # Сохранение данных в базу данных с формы не связанной с моделью
            # print(form.cleaned_data)
            # title = form.cleaned_data['title']
            # Products.objects.create(title=title)
            # product = Products.objects.create(**form.cleaned_data)
            # return redirect(to=product)
            product = form.save()
            return redirect(product)
    else:
        form = ProductsForm()
    return render(request=request, template_name='products/add_product.html', context={'form': form})