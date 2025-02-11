# Generated by Django 5.1.4 on 2025-01-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelterapp', '0013_alter_pet_options_alter_pet_arrival_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='category',
            field=models.CharField(choices=[('Домашнее', 'Домашнее'), ('Дикое', 'Дикое')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pet',
            name='family',
            field=models.CharField(choices=[('Домашнее', [('Кошки', 'Кошки'), ('Собаки', 'Собаки'), ('Грызуны', 'Грызуны'), ('Птицы', 'Птицы')]), ('Дикое', [('Рептилии', 'Рептилии'), ('Другое', 'Другое')])], max_length=50),
        ),
    ]
