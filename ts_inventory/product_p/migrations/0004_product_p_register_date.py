# Generated by Django 3.0.4 on 2020-03-09 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product_p', '0003_auto_20200309_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_p',
            name='register_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
