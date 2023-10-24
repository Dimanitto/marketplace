import logging

import requests

from datetime import datetime
from core import models, consts

logger = logging.getLogger('__name__')


def update_order(order: models.Order) -> None:
    """Обновление заказа"""
    order.date_accept = datetime.now()
    order.status = consts.ORDER_STATUS_CONFIRMED
    order.save(update_fields=('date_accept', 'status'))
    send_order(order)


def send_order(order: models.Order) -> None:
    """Отправка заказа на сторонний сервис"""
    try:
        response = requests.post(
            url='https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4',
            json={
                'id': order.id,
                'amount': float(order.total_sum),
                'date': order.date_accept.isoformat(),
            },
            timeout=10,
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f'Произошла ошибка:', e)
