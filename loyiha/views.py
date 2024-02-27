from rest_framework import generics, permissions
from .models import Shop, Product, Category
from .permissions import HasRolePermission, HasRolePermissionPost
from loyiha import serializer

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ShopAdminView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = serializer.ShopSerializer

    permission_classes = [permissions.IsAuthenticated, HasRolePermission]
    required_roles = ['shop_admin']

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','shops__title']



class ShopUpdateApiView(generics.UpdateAPIView):
    serializer_class = serializer.ShopSerializer
    queryset = Shop.objects.all()

    lookup_field = 'pk'

    permission_classes = [permissions.IsAuthenticated, HasRolePermissionPost]
    required_roles = ['shop_admin']


class ProductListApiview(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializer.ProductSerializer

    permission_classes = [permissions.IsAuthenticated, HasRolePermission]
    required_roles = ['product_admin', 'shop_admin']

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title',]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', "id"]


class UpdateProductApiView(generics.UpdateAPIView):
    serializer_class = serializer.ProductSerializer
    queryset = Product.objects.all()

    lookup_field = 'pk'

    permission_classes = [permissions.IsAuthenticated, HasRolePermissionPost]
    required_roles = ['product_admin']