ORDER_STATUS_CONFIRMED = 'confirmed'
ORDER_STATUS_NEW = 'new'

ORDER_STATUS_CHOICES = (
    (ORDER_STATUS_CONFIRMED, 'Подтвержден'),
    (ORDER_STATUS_NEW, 'Новый'),
)

PAYMENT_STATUS_PAID = 'paid'
PAYMENT_STATUS_REJECTED = 'rejected'
PAYMENT_STATUS_PROCESSING = 'processing'

PAYMENT_STATUS_CHOICES = (
    (PAYMENT_STATUS_PAID, 'Оплачен'),
    (PAYMENT_STATUS_PROCESSING, 'В обработке'),
    (PAYMENT_STATUS_REJECTED, 'Отклонен'),
)

PAYMENT_TYPE_CARD = 'card'
PAYMENT_TYPE_CASH = 'cash'
PAYMENT_TYPE_TRANSFER = 'transfer'
PAYMENT_TYPE_E_WALLET = 'e_wallet'

PAYMENT_TYPE_CHOICES = (
    (PAYMENT_TYPE_CARD, 'Банковская картра'),
    (PAYMENT_TYPE_CASH, 'Наличиные'),
    (PAYMENT_TYPE_TRANSFER, 'Перевод'),
    (PAYMENT_TYPE_E_WALLET, 'Электронный кошелек'),
)
