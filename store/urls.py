from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Affiche la liste des produits


]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Affiche la liste des produits
    path('category/<int:category_id>/', views.category_products, name='category_products'),  # Affiche les produits par catégorie
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Détails du produit
]


