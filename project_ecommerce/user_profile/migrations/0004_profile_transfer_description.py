# Generated by Django 4.2.4 on 2023-10-13 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_alter_shippingfee_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='transfer_description',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
    ]
