# Generated by Django 5.1.1 on 2024-09-28 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_user_remove_payment_delayed_value_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credit',
            name='Created_at',
        ),
    ]