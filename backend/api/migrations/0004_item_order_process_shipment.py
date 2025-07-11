# Generated by Django 5.2.4 on 2025-07-11 00:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_location_product_transaction_delete_book_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='processing', max_length=20)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item')),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('done', 'Done')], default='pending', max_length=20)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('type', models.CharField(choices=[('IN', 'Incoming'), ('OUT', 'Outgooing')], max_length=10)),
                ('date', models.TimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item')),
            ],
        ),
    ]
