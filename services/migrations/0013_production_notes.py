# Generated by Django 3.1.6 on 2021-03-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_auto_20210313_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='notes',
            field=models.CharField(default='tell me more', max_length=320),
            preserve_default=False,
        ),
    ]