# Generated by Django 5.1.1 on 2024-09-28 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_credit_credit_id_remove_payment_payment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Payment_STATUS',
            field=models.CharField(choices=[('pending', 'Pending'), ('delayed', 'Delayed'), ('completed', 'Completed')], max_length=10),
        ),
    ]