# Generated by Django 3.2.6 on 2022-02-11 14:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220211_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcolor',
            name='sizes',
        ),
        migrations.AddField(
            model_name='productcolor',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memory_products', to='app.memory', verbose_name='Память'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 11, 14, 46, 33, 583078, tzinfo=utc), verbose_name='Дата создания'),
        ),
    ]