# Generated by Django 3.2.5 on 2021-08-08 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210807_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramusermodel',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='telegramusermodel',
            name='number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
