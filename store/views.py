from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'categories': categories, 'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})


from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_products(request, category_id):
    # Récupérer la catégorie par son id
    category = get_object_or_404(Category, id=category_id)
    # Récupérer les produits associés à cette catégorie
    products = Product.objects.filter(category=category)
    return render(request, 'store/category_products.html', {'category': category, 'products': products})

# Create your views here.
