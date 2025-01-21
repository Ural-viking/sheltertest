from django.db import models
from django.contrib.auth.models import User

class Shelter(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='shelter_photos/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shelters')

    def __str__(self):
        return self.name
    
class UserShelter(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
        
        class Meta:
            unique_together = ('user', 'shelter')
            
class Pet(models.Model):
    CATEGORY_CHOICES = [
        ('Домашнее', 'Домашнее'),
        ('Дикое', 'Дикое'),
        ('Экзотическое', 'Экзотическое'),
    ]

    FAMILY_CHOICES = [
        ('Кошки', 'Кошки'),
        ('Собаки', 'Собаки'),
        ('Грызуны', 'Грызуны'),
        ('Птицы', 'Птицы'),
        ('Рептилии', 'Рептилии'),
        ('Другое', 'Другое'),
    ]

    BREED_CHOICES = {
        'Кошки': [
            ('Сиамская', 'Сиамская'),
            ('Мейн-кун', 'Мейн-кун'),
            ('Сфинкс', 'Сфинкс'),
        ],
        'Собаки': [
            ('Немецкая овчарка', 'Немецкая овчарка'),
            ('Такса', 'Такса'),
            ('Французский бульдог', 'Французский бульдог'),
        ],
        'Грызуны': [
            ('Хомяк', 'Хомяк'),
            ('Крыса', 'Крыса'),
            ('Морская свинка', 'Морская свинка'),
        ],
        'Птицы': [
            ('Попугай', 'Попугай'),
            ('Канарейка', 'Канарейка'),
            ('Волнистый попугайчик', 'Волнистый попугайчик'),
        ],
        'Рептилии': [
            ('Игуана', 'Игуана'),
            ('Удав', 'Удав'),
            ('Черепаха', 'Черепаха'),
        ],
        'Другое': [
            ('Другое', 'Другое'),
        ],
    }

    SIZE_CHOICES = [
        ('Крупный', 'Крупный'),
        ('Средний', 'Средний'),
        ('Мелкий', 'Мелкий'),
    ]
    
    GENDER_CHOICES = [
        ('Мужской','Мужской'),
        ('Женский','Женский'),
    ]

    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    family = models.CharField(max_length=50, choices=FAMILY_CHOICES)
    breed = models.CharField(max_length=255, choices=BREED_CHOICES)
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    arrival_date = models.DateField()
    photo = models.ImageField(upload_to='pet_photos/', blank=True, null=True)

    def __str__(self):
        return self.name