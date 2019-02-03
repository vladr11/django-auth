from rest_framework import viewsets
from rest_framework import permissions

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    View that any authenticated user should be able to CRUD.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
