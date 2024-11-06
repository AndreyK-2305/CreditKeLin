# Generated by Django 5.1.1 on 2024-11-06 01:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '__first__'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_STATUS', models.CharField(choices=[('pending', 'Pending'), ('delayed', 'Delayed'), ('completed', 'Completed')], max_length=10)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('delayed_value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('started', 'Started'), ('active', 'Active'), ('completed', 'Completed'), ('suspended', 'Suspended')], max_length=10)),
                ('client', models.ForeignKey(default=0, on_delete=django.db.models.deletion.RESTRICT, to='users.user')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.product')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='credit.payment')),
            ],
        ),
    ]
