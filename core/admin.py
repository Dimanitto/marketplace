from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from core import models, consts
from core.datatools.order import update_order


@admin.register(models.Product)
class Product(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    search_help_text = 'Поиск по названию'


@admin.register(models.Order)
class Order(admin.ModelAdmin):
    list_display = ('status', 'total_sum', 'date_create', 'date_accept')
    list_filter = ('status',)
    readonly_fields = ('status', 'date_accept', 'date_create')
    search_fields = ('date_create',)
    search_help_text = 'Поиск по дате создания'

    change_form_template = 'admin/core/custom_view.html'

    def response_change(
            self, request: WSGIRequest, obj: models.Order
    ) -> None:
        if "confirm" in request.POST:
            update_order(obj)
        return super().response_change(request, obj)

    def change_view(
            self, request: WSGIRequest, object_id: int,
            form_url: str = "", extra_context: dict = None
    ) -> None:
        extra_context = extra_context or {}
        order = models.Order.objects.get(id=object_id)
        if (
                hasattr(order, 'payment') and
                order.payment.status == consts.PAYMENT_STATUS_PAID and
                order.date_accept is None
        ):
            extra_context['show_button'] = True
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )


@admin.register(models.Payment)
class Payment(admin.ModelAdmin):
    list_display = ('status', 'sum', 'type', 'order')
    list_filter = ('status', 'type')


@admin.register(models.OrderProduct)
class OrderProduct(admin.ModelAdmin):
    list_display = ('product', 'order', 'amount')
