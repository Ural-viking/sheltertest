# Generated by Django 5.1.4 on 2025-01-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelterapp', '0005_alter_pet_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.CharField(choices=[('Кошки', [('Сиамская', 'Сиамская'), ('Мейн-кун', 'Мейн-кун'), ('Сфинкс', 'Сфинкс')]), ('Собаки', [('Австралийская овчарка', 'Австралийская овчарка'), ('Австралийская пастушья собака', 'Австралийская пастушья собака'), ('Азавак', 'Азавак'), ('Акита-ину', 'Акита-ину'), ('Алабай', 'Алабай'), ('Аляскинский кли-кай', 'Аляскинский кли-кай'), ('Аляскинский маламут', 'Аляскинский маламут'), ('Американская акита', 'Американская акита'), ('Американский бандог', 'Американский бандог'), ('Американский булли', 'Американский булли'), ('Американский бульдог', 'Американский бульдог'), ('Американский голый терьер', 'Американский голый терьер'), ('Американский кокер-спаниель', 'Американский кокер-спаниель'), ('Американский стаффордширский терьер', 'Американский стаффордширский терьер'), ('Английский бульдог', 'Английский бульдог'), ('Английский кокер-спаниель', 'Английский кокер-спаниель'), ('Английский мастиф', 'Английский мастиф'), ('Английский пойнтер', 'Английский пойнтер'), ('Английский сеттер', 'Английский сеттер'), ('Английский той-терьер', 'Английский той-терьер'), ('Английский фоксхаунд', 'Английский фоксхаунд'), ('Аппенцеллер зенненхунд', 'Аппенцеллер зенненхунд'), ('Аргентинский дог', 'Аргентинский дог'), ('Афганская борзая', 'Афганская борзая'), ('Аффенпинчер', 'Аффенпинчер'), ('Банхар', 'Банхар'), ('Басенджи', 'Басенджи'), ('Бассет-хаунд', 'Бассет-хаунд'), ('Бедлингтон-терьер', 'Бедлингтон-терьер'), ('Белая швейцарская овчарка', 'Белая швейцарская овчарка'), ('Бельгийская овчарка', 'Бельгийская овчарка'), ('Бельгийский гриффон', 'Бельгийский гриффон'), ('Бернский зенненхунд', 'Бернский зенненхунд'), ('Бивер-йоркширский терьер', 'Бивер-йоркширский терьер'), ('Бигль', 'Бигль'), ('Бишон фризе', 'Бишон фризе'), ('Бладхаунд', 'Бладхаунд'), ('Бобтейл', 'Бобтейл'), ('Боксер', 'Боксер'), ('Большой швейцарский зенненхунд', 'Большой швейцарский зенненхунд'), ('Бордер-колли', 'Бордер-колли'), ('Бордер-терьер', 'Бордер-терьер'), ('Бордоский дог', 'Бордоский дог'), ('Босерон', 'Босерон'), ('Немецкая овчарка', 'Немецкая овчарка'), ('Такса', 'Такса'), ('Французский бульдог', 'Французский бульдог')]), ('Грызуны', [('Хомяк', 'Хомяк'), ('Крыса', 'Крыса'), ('Морская свинка', 'Морская свинка')]), ('Птицы', [('Попугай', 'Попугай'), ('Канарейка', 'Канарейка'), ('Волнистый попугайчик', 'Волнистый попугайчик')]), ('Рептилии', [('Игуана', 'Игуана'), ('Удав', 'Удав'), ('Черепаха', 'Черепаха')]), ('Другое', [('Другое', 'Другое')])], max_length=255),
        ),
    ]
