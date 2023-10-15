# Generated by Django 4.2.4 on 2023-10-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_remove_order_shipping_fee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]