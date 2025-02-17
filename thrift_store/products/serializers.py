from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'description',
            # 'seller_id',
            # 'price',
            # 'pictures',
            # 'posted_on',
        )
