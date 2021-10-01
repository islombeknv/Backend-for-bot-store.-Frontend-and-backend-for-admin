# Generated by Django 3.2.5 on 2021-08-07 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20210807_1355'),
        ('service', '0004_auto_20210807_1523'),
        ('orders', '0002_delete_ordermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(choices=[('one', 'one1'), ('two', 'two2'), ('three', 'three2')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.telegramusermodel')),
                ('products', models.ManyToManyField(related_name='order', to='service.ServiceModel')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
    ]
