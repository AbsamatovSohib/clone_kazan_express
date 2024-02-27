from rest_framework import serializers
from .models import Shop, Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "amount",
            "price",
            "image",
            "active",
        )


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "title",
            "description",
            "amount",
            "price",
            "image",
            "active",
        )


class CategorySerializer(serializers.ModelSerializer):
    categories = ProductSerializer(many=True,read_only=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "description",
            "categories",
        )


class ShopSerializer(serializers.ModelSerializer):
    shops = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = (
            "id",
            "title",
            "description",
            "imageurl",
            "owner",
            "shops",
        )


class ShopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            "title",
            "description",
            "imageurl",
            "owner",
        )