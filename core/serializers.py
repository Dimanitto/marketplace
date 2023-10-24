from rest_framework import serializers

from core import models


class Product(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class OrderProduct(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset=models.Product.objects.all(),
        source='product'
    )

    class Meta:
        model = models.OrderProduct
        fields = ('id', 'amount')


class Order(serializers.ModelSerializer):
    products = OrderProduct(many=True, source='order_products')

    class Meta:
        model = models.Order
        fields = '__all__'
        read_only_fields = ('status', 'total_sum', 'date_accept')

    def create(self, validated_data: dict) -> models.Order:
        """Посчитаем сумму заказа и создаим заказ"""
        order_products = validated_data.pop('order_products', [])
        total_sum = sum(
            product.get('amount', 1) * product['product'].price
            for product in order_products
        )
        order = models.Order.objects.create(total_sum=total_sum)
        products_id = [product['product'].id for product in order_products]
        models.OrderProduct.objects.bulk_create(
            models.OrderProduct(
                product=product['product'],
                order=order,
                amount=product.get('amount', 1)
            )
            for product in order_products
        )
        order.products.set(products_id)
        return order


class Payment(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = '__all__'
        read_only_fields = ('sum',)
