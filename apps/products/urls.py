from django.urls import path
from . import views

urlpatterns = [
    # path("", products, name="products"),    
    # path("", views.create_list_product),
    path("<int:pk>/", views.detail_product),
    path("<int:pk>/update/", views.update_product),
    path("<int:pk>/delete/", views.delete_product),
    path("", views.create_list_product),
]