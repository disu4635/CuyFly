# Generated by Django 5.0.1 on 2024-01-18 23:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuy_app', '0004_alter_ticket_email_alter_ticket_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
