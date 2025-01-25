from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .models import Shelter, Pet
from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': _('Обязательное поле. Не более 150 символов. Только буквы, цифры и @/./+/-/_.'),
        }
        error_messages = {
            'username': {
                'required': _("Это поле обязательно."),
                'max_length': _("Имя пользователя не может быть длиннее 150 символов."),
                'invalid': _("Введите корректное имя пользователя. Только буквы, цифры и @/./+/-/_."),
            },
            'email': {
                'required': _("Это поле обязательно."),
                'invalid': _("Введите корректный адрес электронной почты."),
            },
            'password1': {
                'required': _("Это поле обязательно."),
            },
            'password2': {
                'required': _("Это поле обязательно."),
            },
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_("Имя пользователя:"), max_length=150, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=_("Пароль:"), widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': _("Пожалуйста, введите правильное имя пользователя и пароль. Обратите внимание, что оба поля могут быть чувствительны к регистру."),
        'inactive': _("Этот аккаунт отключен."),
    }
        
class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = ['name', 'address', 'description', 'photo']
        labels = {
            'name': _('Название'),
            'address': _('Адрес'),
            'description': _('Описание'),
            'photo': _('Фото'),
        }
        help_texts = {
            'name': _('Введите название приюта.'),
            'address': _('Введите адрес приюта.'),
            'description': _('Введите описание приюта.'),
            'photo': _('Загрузите фото приюта.'),
        }
        error_messages = {
            'name': {
                'required': _("Это поле обязательно."),
            },
            'address': {
                'required': _("Это поле обязательно."),
            },
        }
        
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254)

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'category', 'family', 'breed', 'gender', 'size', 'arrival_date', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.data:
            category = self.data.get('category')
            families = Pet.DOMESTIC_FAMILY_CHOICES if category == 'Домашнее' else Pet.WILD_FAMILY_CHOICES
            self.fields['family'].choices = families
            if 'family' in self.data:
                family = self.data.get('family')
                breeds = Pet.BREED_CHOICES.get(family, [])
                self.fields['breed'].choices = breeds
        elif self.instance.pk:
            families = Pet.DOMESTIC_FAMILY_CHOICES if self.instance.category == 'Домашнее' else Pet.WILD_FAMILY_CHOICES
            self.fields['family'].choices = families
            breeds = Pet.BREED_CHOICES.get(self.instance.family, [])
            self.fields['breed'].choices = breeds