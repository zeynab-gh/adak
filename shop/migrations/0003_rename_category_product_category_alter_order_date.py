# Generated by Django 5.1.1 on 2024-09-19 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_product_category_alter_order_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='Category',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 19, 14, 47, 35, 787720)),
        ),
    ]