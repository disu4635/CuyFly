# Generated by Django 5.0.1 on 2024-01-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuy_app', '0003_ticket_seat_alter_flight_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='email',
            field=models.EmailField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
