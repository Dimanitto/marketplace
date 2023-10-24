from django.db import models

from core import consts


class Product(models.Model):
    name = models.CharField('Название', max_length=255)
    image = models.ImageField('Картинка', upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    total_sum = models.DecimalField('Итоговая сумма', max_digits=10, decimal_places=2)
    status = models.CharField(
        'Статус', max_length=255,
        choices=consts.ORDER_STATUS_CHOICES,
        default=consts.ORDER_STATUS_NEW,
    )
    products = models.ManyToManyField(
        Product, verbose_name='Товары', related_name='orders', through='OrderProduct'
    )
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_accept = models.DateTimeField('Дата подтверждения', blank=True, null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date_create']
        indexes = [
            models.Index(fields=['-date_create'])
        ]

    def __str__(self) -> str:
        return f'{self.date_create} - {self.status}'


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,
        verbose_name='Заказ', related_name='order_products'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        verbose_name='Товар', related_name='order_products'
    )
    amount = models.PositiveIntegerField('Количество', blank=True, default=1)

    class Meta:
        verbose_name = 'Количество товаров в заказе'
        verbose_name_plural = 'Количество товаров в заказе'


class Payment(models.Model):
    sum = models.DecimalField('Сумма', max_digits=10, decimal_places=2)
    order = models.OneToOneField(Order, verbose_name='Заказ', related_name='payment', on_delete=models.PROTECT)
    status = models.CharField(
        'Статус', max_length=255,
        choices=consts.PAYMENT_STATUS_CHOICES,
        default=consts.PAYMENT_STATUS_PROCESSING,
    )
    type = models.CharField(
        'Тип оплаты', max_length=255,
        choices=consts.PAYMENT_TYPE_CHOICES
    )

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self) -> str:
        return f'{self.sum} - {self.status}'
