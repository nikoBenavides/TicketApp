# Generated by Django 3.2.8 on 2022-01-19 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20220118_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='deliveryDate',
            field=models.DateField(null=True),
        ),
    ]
