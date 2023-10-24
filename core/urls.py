from django.urls import path
from rest_framework.routers import DefaultRouter

from core import views

app_name = 'core'

urlpatterns = [
    path('order_create/', views.OrderView.as_view(), name='order_create'),
    path('payment_create/', views.PaymentView.as_view(), name='payment_create'),
]

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')

urlpatterns += router.urls
