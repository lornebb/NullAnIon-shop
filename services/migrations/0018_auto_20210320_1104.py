# Generated by Django 3.1.6 on 2021-03-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_auto_20210319_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mix',
            name='order_total',
            field=models.DecimalField(decimal_places=2, default=22.23, max_digits=10),
        ),
    ]
