# Generated by Django 4.2.10 on 2024-05-09 07:52

import booking.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='customer_email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='customer_firstname',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='customer_lastname',
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default=booking.models.get_def_model_id, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]