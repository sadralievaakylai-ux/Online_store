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

def product_add_view(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.POST.get('image')
        category_id = request.POST.get('category')
        description = request.POST.get('description')

        category = get_object_or_404(Category, pk=category_id)

        product = Product.objects.create(
            name=name,
            price=price,
            image=image,
            category=category,
            description=description
        )

        return redirect('product', pk=product.pk)

    return render(request, 'product_add.html', { 'categories': categories })