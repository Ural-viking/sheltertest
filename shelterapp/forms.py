from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .models import Shelter, Pet, VetAssignment, PetVetAssignment
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
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
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

class VetAssignmentForm(forms.ModelForm):
    class Meta:
        model = VetAssignment
        fields = ['diagnosis', 'medication', 'dosage', 'frequency', 'duration', 'document']
        labels = {
            'diagnosis':_('Диагноз'),
            'medication':_('Необходимые лекарства'),
            'dosage':_('Дозировка в граммах'),
            'frequency':_('Сколько раз в день'),
            'duration':_('Продолжительность лечения'),
            'document':_('Документ'),
        }

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'category', 'family', 'breed', 'gender', 'size', 'arrival_date', 'photo']
        widgets = {
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'name': 'Кличка',
            'category': 'Категория',
            'family': 'Класс или семейство',
            'breed': 'Порода',
            'gender': 'Пол',
            'size': 'Размер',
            'arrival_date': 'Дата появления в приюте',
            'photo': 'Фото питомца',
            
        }
        error_messages = {
            'name': {
                'required':_("Это поле обязательно"),
            },
            'category': {
                'required':_("Это поле обязательно"),
            },
            'family': {
                'required': 'Это поле обязательно.',
            },
            'breed': {
                'required': 'Это поле обязательно.',
            },
            'gender': {
                'required': 'Это поле обязательно.',
            },
            'size': {
                'required': 'Это поле обязательно.',
            },
            'arrival_date': {
                'required': 'Это поле обязательно.',
            },
            'photo': {
                'required': 'Это поле обязательно.',
            },
        }
        
    
    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)
        self.fields['family'].widget = forms.Select()
        self.fields['breed'].widget = forms.Select()
        
        if 'category' in self.data:
            category = self.data.get('category')
            self.fields['family'].choices = Pet.FAMILY_CHOICES.get(category, [])
        elif self.instance.pk:
            category = self.instance.category
            self.fields['family'].choices = Pet.FAMILY_CHOICES.get(category, [])
        
        if 'family' in self.data:
            family = self.data.get('family')
            self.fields['breed'].choices = Pet.BREED_CHOICES.get(family, [])
        elif self.instance.pk:
            family = self.instance.family
            self.fields['breed'].choices = Pet.BREED_CHOICES.get(family, [])

class PetVetAssignmentForm(forms.ModelForm):
    class Meta:
        model = PetVetAssignment
        fields = ['pet', 'vet_assignment']