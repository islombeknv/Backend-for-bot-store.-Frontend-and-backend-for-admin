# Generated by Django 3.2.5 on 2021-08-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20210807_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='pid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
