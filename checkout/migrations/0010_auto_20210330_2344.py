# Generated by Django 3.1.7 on 2021-03-30 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20210330_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_production',
            name='production_type',
            field=models.CharField(choices=[('guitar', 'Guitar'), ('bass', 'Bass'), ('synths', 'Synths'), ('piano', 'Piano'), ('drums', 'Drums'), ('track_production', 'Track Production')], default='', max_length=1026),
        ),
    ]