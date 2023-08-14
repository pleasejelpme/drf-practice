from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveAPIView, 
    ListCreateAPIView, 
    RetrieveUpdateAPIView, 
    RetrieveDestroyAPIView,
    GenericAPIView
    )
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .permissions import StaffEditorPermitions
from .models import Product
from .serializers import ProductSerializer


# @api_view(['GET', 'POST'])
# def products(request, *args, **kwargs):
#     if request.method == 'GET':
#         instance = Product.objects.all()
#         data = ProductSerializer(instance, many=True).data
#         return Response(data)

#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             product = serializer.save()
#             print(product)
#             return Response(serializer.data)
#         return Response({'error':'Invalid data'}, status=400)


# LIST AND CREATE PRODUCTS
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    authentication_classes = [
        SessionAuthentication, 
        TokenAuthentication]
    permission_classes = [StaffEditorPermitions]   

    def get_queryset(self):
        request = self.request
        print(request.user)
        return super().get_queryset()


# DETAIL PRODUCT
class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    permission_classes = [StaffEditorPermitions]

# UPDATE PRODUCT
class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [StaffEditorPermitions]
    

# DELETE PRODUCT
class ProductDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [StaffEditorPermitions] 




# Renaming views for urls
create_list_product = ProductListCreateAPIView.as_view()
detail_product = ProductDetailAPIView.as_view()
update_product = ProductUpdateAPIView.as_view()
delete_product = ProductDestroyAPIView.as_view()
