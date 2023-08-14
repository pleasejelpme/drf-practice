from django.urls import path
from . import views

urlpatterns = [
    # path("", products, name="products"),    
    # path("", views.create_list_product),
    path("<int:pk>/", views.detail_product, name='product-detail'),
    path("<int:pk>/update/", views.update_product, name='product-update'),
    path("<int:pk>/delete/", views.delete_product, name='product-delete'),
    path("", views.create_list_product, name='product-list'),
]