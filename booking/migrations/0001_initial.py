# Generated by Django 3.2.8 on 2021-12-28 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinema', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.PositiveIntegerField()),
                ('row', models.PositiveIntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='cinema.room')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_card', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('payment_method', models.CharField(choices=[('card', 'card'), ('mobile', 'mobile'), ('e-Wallet', 'e-Wallet')], max_length=255)),
                ('payment_value', models.CharField(max_length=200)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.discount')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.seat')),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.showtime')),
                ('ticket_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.tickettype')),
            ],
        ),
    ]