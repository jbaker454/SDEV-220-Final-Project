# Generated by Django 5.2.4 on 2025-07-15 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_transaction_product_transaction_resource_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='api.location'),
            preserve_default=False,
        ),
    ]
