# Generated by Django 3.2.3 on 2021-06-01 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maxway', '0002_auto_20210530_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='foods',
            field=models.ManyToManyField(blank=True, related_name='_maxway_product_foods_+', to='maxway.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]