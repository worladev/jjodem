# Generated by Django 4.2.10 on 2024-04-19 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0003_cartype_is_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialhandle',
            old_name='handle_name',
            new_name='platform',
        ),
    ]
