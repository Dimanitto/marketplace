from rest_framework import viewsets, generics

from core import models, serializers


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.Product


class OrderView(generics.CreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.Order


class PaymentView(generics.CreateAPIView):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.Payment

    def perform_create(self, serializer: serializers.Payment) -> None:
        order = serializer.validated_data.get('order')
        serializer.save(sum=order.total_sum)
