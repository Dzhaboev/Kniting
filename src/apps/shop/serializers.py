from rest_framework import serializers

from src.apps.shop.models import Product, Category, OrderCartItem, OrderCart, ProductColor


# TODO: убрать
class ProductSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'title',
            'slug',
            'price',
            'sale',
            'author',
            'image_preview',
            'image_alt',
        )
        
        
class CategoryRetrieveSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = (
            'title',
            'slug',
            'title_seo',
            'meta_keywords',
            'meta_description',
            'products'

        )
        
    def get_products(self, obj):
        products = Product.objects.filter(categories=obj, is_active=True)
        return ProductListSerializer(products, many=True).data
    

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'title',
            'slug',
        )


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ('color',)


class ProductRetrieveSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True, read_only=True)
    colors = ColorSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'code',
            'title',
            'slug',
            'description',
            'price',
            'sale',
            'categories',
            'author',
            'count',
            'type_product',
            'material',
            'included',
            'height',
            'weight',
            'colors',
            # ImagesMixin
            'image_preview',
            'image_alt',
            # SeoMixin
            'title_seo',
            'meta_keywords',
            'meta_description',
            'created_at',
            'update_at'
        )


class ProductListSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True, read_only=True)
    colors = ColorSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'price',
            'sale',
            'colors',
            'categories',
            'author',
            'image_preview',
            'image_alt',
        )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCartItem
        fields = ('pk', 'product', 'amount')


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True)

    class Meta:
        model = OrderCart
        fields = ('pk', 'products', 'phone', 'address', 'comments',)

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = OrderCart.objects.create(**validated_data)
        for product_data in products_data:
            OrderCartItem.objects.create(**product_data)
        return order