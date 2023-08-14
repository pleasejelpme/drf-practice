from rest_framework.routers import DefaultRouter
from apps.products.viewsets import ProductViewSet

from django.urls import path

router = DefaultRouter()
router.register('products-abc', ProductViewSet, basename='products')
urlpatterns = router.urls