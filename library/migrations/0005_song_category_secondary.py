# Generated by Django 3.1.6 on 2021-03-01 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20210301_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='category_secondary',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
