# Generated by Django 5.1.7 on 2025-05-05 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_carmodel_base_price_alter_carmodel_created_by'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactForm',
        ),
    ]
