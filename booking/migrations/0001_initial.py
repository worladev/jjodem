# Generated by Django 4.2.10 on 2024-05-05 21:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rentals', '0002_alter_shopinfo_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_firstname', models.CharField(max_length=25)),
                ('customer_lastname', models.CharField(max_length=25)),
                ('customer_email', models.EmailField(max_length=50)),
                ('start_date', models.DateField(db_index=True)),
                ('end_date', models.DateField(db_index=True)),
                ('booking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('paid', models.BooleanField(default=False)),
                ('car_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.carmodel')),
            ],
            options={
                'ordering': ['-booking_date'],
                'indexes': [models.Index(fields=['start_date', 'end_date'], name='booking_boo_start_d_97bc99_idx')],
            },
        ),
    ]
