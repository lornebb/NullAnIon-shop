# Generated by Django 3.1.6 on 2021-03-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_production_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='mix_extras',
            field=models.CharField(blank=True, choices=[('Drum Replacement', 'Drum Replacement'), ('Instrumental Version', 'Instruemntal Version'), ('Show Ready Version', 'Show Ready Version'), ('A Capella Version', 'A Capella Version')], default='Instrumental Version', max_length=1026),
        ),
        migrations.AlterField(
            model_name='master',
            name='package_type',
            field=models.CharField(choices=[('single (< 5mins)', 'single (< 5mins)'), ('ep (< 35mins)', 'ep (< 35mins)'), ('album / LP (> 35mins)', 'album / LP (> 35mins)')], default='single (< 5mins)', max_length=1026),
        ),
        migrations.AlterField(
            model_name='master',
            name='reference_link_type',
            field=models.CharField(blank=True, choices=[('general', 'general'), ('energy', 'energy'), ('tone', 'tone'), ('instrument', 'instrument')], max_length=1026),
        ),
        migrations.AlterField(
            model_name='master',
            name='revisions',
            field=models.CharField(choices=[('3', '3'), ('6', '6')], default=3, max_length=1026),
        ),
        migrations.AlterField(
            model_name='master',
            name='stem_choices',
            field=models.CharField(choices=[('max 5 grouped stems', 'max 5 grouped stems'), ('Individual track stems', 'individual track stems')], default=['max 5 grouped stems'], max_length=1026),
        ),
        migrations.AlterField(
            model_name='master',
            name='order_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='mix',
            name='package_type',
            field=models.CharField(choices=[('single (< 5mins)', 'single (< 5mins)'), ('ep (< 35mins)', 'ep (< 35mins)'), ('album / LP (> 35mins)', 'album / LP (> 35mins)')], default='single (< 5mins)', max_length=1026),
        ),
        migrations.AlterField(
            model_name='mix',
            name='reference_link_type',
            field=models.CharField(blank=True, choices=[('general', 'general'), ('energy', 'energy'), ('tone', 'tone'), ('instrument', 'instrument')], max_length=1026),
        ),
        migrations.AlterField(
            model_name='mix',
            name='revisions',
            field=models.CharField(choices=[('3', '3'), ('6', '6')], default=3, max_length=1026),
        ),
        migrations.AlterField(
            model_name='mix',
            name='stem_choices',
            field=models.CharField(choices=[('6', '6'), ('40', '40'), ('40+', '40+')], default=6, max_length=1026),
        ),
    ]
