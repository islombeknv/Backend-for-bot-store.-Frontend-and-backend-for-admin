# Generated by Django 3.2.5 on 2021-08-08 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_ordermodel_pid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='pid',
            new_name='p_id',
        ),
    ]