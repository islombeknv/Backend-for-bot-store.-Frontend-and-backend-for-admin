# Generated by Django 3.2.5 on 2021-08-09 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_ordermodel_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='address',
            field=models.CharField(max_length=15),
        ),
    ]
