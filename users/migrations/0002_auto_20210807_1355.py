# Generated by Django 3.2.5 on 2021-08-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.IntegerField(unique=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Telegram user',
                'verbose_name_plural': 'Telegram users',
            },
        ),
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
