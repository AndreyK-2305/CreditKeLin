# Generated by Django 5.1.1 on 2024-09-28 01:05

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_credit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_id', models.IntegerField()),
                ('Payment_STATUS', models.CharField(choices=[('pending', 'Pending'), ('complete', 'Complete'), ('delayed', 'Delayed')], max_length=10)),
                ('value', models.IntegerField()),
                ('Delayed_value', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='credit',
            name='Payment_id',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='products.payment'),
            preserve_default=False,
        ),
    ]
