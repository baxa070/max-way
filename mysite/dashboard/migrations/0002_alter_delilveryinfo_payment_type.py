# Generated by Django 3.2.3 on 2021-06-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delilveryinfo',
            name='payment_type',
            field=models.CharField(default=0, max_length=100),
        ),
    ]