# Generated by Django 5.0.1 on 2024-01-23 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_stock_ticker'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
