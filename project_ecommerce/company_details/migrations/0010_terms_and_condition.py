# Generated by Django 4.2.4 on 2023-10-13 12:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_details', '0009_account_detail_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terms_and_condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(default='Terms and conditions')),
            ],
        ),
    ]