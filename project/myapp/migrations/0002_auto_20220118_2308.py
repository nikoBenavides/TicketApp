# Generated by Django 3.2.8 on 2022-01-19 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='beginDate',
            field=models.DateTimeField(null=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loan',
            name='endDate',
            field=models.DateTimeField(null=True),
            preserve_default=False,
        ),
    ]