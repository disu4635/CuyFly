# Generated by Django 5.0.1 on 2024-01-18 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuy_app', '0002_flight_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='seat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='cuy_app.seat'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.CharField(default='0', max_length=40),
        ),
    ]
