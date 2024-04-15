# Generated by Django 5.0.3 on 2024-04-15 11:29

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapi', '0004_customer_alter_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.ImageField(default=1, upload_to='')),
                ('price', models.ImageField(upload_to='')),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapi.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapi.product')),
            ],
        ),
    ]