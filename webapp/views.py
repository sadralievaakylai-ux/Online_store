from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product, Category

def products_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product': product})

def category_add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')

        if Category.objects.filter(name=name).exists():
            return render(request, 'category_add.html', {
                'error': 'Такая категория уже существует'
            })

        Category.objects.create(
            name=name,
            description=description
        )

        return redirect('products')

    return render(request, 'category_add.html')