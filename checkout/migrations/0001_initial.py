# Generated by Django 3.1.7 on 2021-03-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('order_type', models.CharField(default='', max_length=20)),
                ('package_type', models.CharField(default='', max_length=50)),
                ('deliver_by', models.DateTimeField(auto_now_add=True)),
                ('stem_choices', models.CharField(default=6, max_length=1026)),
                ('revisions', models.CharField(default=3, max_length=1026)),
                ('reference_link_type', models.CharField(blank=True, max_length=1026)),
                ('reference_link', models.URLField(blank=True)),
                ('mix_extras', models.CharField(max_length=1026)),
                ('contact', models.EmailField(default='', max_length=254)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
