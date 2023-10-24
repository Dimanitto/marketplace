# Generated by Django 4.2.6 on 2023-10-24 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итоговая сумма')),
                ('status', models.CharField(choices=[('confirmed', 'Подтвержден'), ('new', 'Новый')], default='new', max_length=255, verbose_name='Статус')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_accept', models.DateTimeField(blank=True, null=True, verbose_name='Дата подтверждения')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-date_create'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Картинка')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'indexes': [models.Index(fields=['name'], name='core_produc_name_be3252_idx')],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма')),
                ('status', models.CharField(choices=[('paid', 'Оплачен'), ('processing', 'В обработке'), ('rejected', 'Отклонен')], default='processing', max_length=255, verbose_name='Статус')),
                ('type', models.CharField(choices=[('card', 'Банковская картра'), ('cash', 'Наличиные'), ('transfer', 'Перевод'), ('e_wallet', 'Электронный кошелек')], max_length=255, verbose_name='Тип оплаты')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='payment', to='core.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(blank=True, default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='core.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='core.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Количество товаров в заказе',
                'verbose_name_plural': 'Количество товаров в заказе',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', through='core.OrderProduct', to='core.product', verbose_name='Товары'),
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['-date_create'], name='core_order_date_cr_3aefe3_idx'),
        ),
    ]