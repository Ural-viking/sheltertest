# Generated by Django 5.1.4 on 2025-01-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelterapp', '0009_alter_pet_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='category',
            field=models.CharField(choices=[('Домашнее', 'Домашнее'), ('Дикое', 'Дикое')], max_length=10),
        ),
    ]
