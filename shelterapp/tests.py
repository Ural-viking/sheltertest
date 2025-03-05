from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Shelter, Role, UserShelter, UserRole, VetAssignment, Pet, PetVetAssignment
from .forms import RegisterForm, LoginForm, ShelterForm, VetAssignmentForm, PetForm

class ModelTests(TestCase):
    def setUp(self):
        # Метод setUp вызывается перед каждым тестом. Здесь мы создаем объекты, которые будут использоваться в тестах.
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.shelter = Shelter.objects.create(name='Test Shelter', address='123 Test St', user=self.user)
        self.role = Role.objects.create(name=Role.ADMIN)
        self.user_shelter = UserShelter.objects.create(user=self.user, shelter=self.shelter)
        self.user_role = UserRole.objects.create(user=self.user, role=self.role)
        self.pet = Pet.objects.create(
            name='Test Pet',
            category='Домашнее',
            family='Кошки',
            breed='Сиамская',
            gender='Мужской',
            size='Средний',
            arrival_date='2023-01-01',
            shelter=self.shelter
        )
        self.vet_assignment = VetAssignment.objects.create(diagnosis='Test Diagnosis')
        self.pet_vet_assignment = PetVetAssignment.objects.create(pet=self.pet, vet_assignment=self.vet_assignment)

    def test_shelter_creation(self):
        # Проверяем, что объект Shelter создается правильно.
        self.assertEqual(self.shelter.name, 'Test Shelter')
        self.assertEqual(self.shelter.user, self.user)

    def test_role_creation(self):
        # Проверяем, что объект Role создается правильно.
        self.assertEqual(self.role.name, Role.ADMIN)

    def test_user_shelter_creation(self):
        # Проверяем, что объект UserShelter создается правильно.
        self.assertEqual(self.user_shelter.user, self.user)
        self.assertEqual(self.user_shelter.shelter, self.shelter)

    def test_user_role_creation(self):
        # Проверяем, что объект UserRole создается правильно.
        self.assertEqual(self.user_role.user, self.user)
        self.assertEqual(self.user_role.role, self.role)

    def test_pet_creation(self):
        # Проверяем, что объект Pet создается правильно.
        self.assertEqual(self.pet.name, 'Test Pet')
        self.assertEqual(self.pet.shelter, self.shelter)

    def test_vet_assignment_creation(self):
        # Проверяем, что объект VetAssignment создается правильно.
        self.assertEqual(self.vet_assignment.diagnosis, 'Test Diagnosis')

    def test_pet_vet_assignment_creation(self):
        # Проверяем, что объект PetVetAssignment создается правильно.
        self.assertEqual(self.pet_vet_assignment.pet, self.pet)
        self.assertEqual(self.pet_vet_assignment.vet_assignment, self.vet_assignment)

class FormTests(TestCase):
    def test_register_form_valid_data(self):
        # Проверяем, что форма регистрации принимает корректные данные.
        form = RegisterForm(data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        self.assertTrue(form.is_valid())

    def test_login_form_valid_data(self):
        # Создаем пользователя для теста
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

        # Проверяем, что форма входа принимает корректные данные.
        form = LoginForm(data={
            'username': 'testuser',
            'password': 'testpassword123',
        })

        # Убедитесь, что форма получает все необходимые данные.
        self.assertTrue(form.is_valid(), f"Form errors: {form.errors}")

    def test_shelter_form_valid_data(self):
        # Проверяем, что форма создания приюта принимает корректные данные.
        form = ShelterForm(data={
            'name': 'New Shelter',
            'address': 'Test Address',
            'description': 'A new shelter',
        })
        self.assertTrue(form.is_valid())

    def test_vet_assignment_form_valid_data(self):
        # Проверяем, что форма назначения ветеринара принимает корректные данные.
        form = VetAssignmentForm(data={
            'diagnosis': 'Test Diagnosis',
            'medication': 'Test Medication',
            'dosage': '100mg',
            'frequency': 'Twice a day',
            'duration': '10 days',
        })
        self.assertTrue(form.is_valid())

    def test_pet_form_valid_data(self):
        # Проверяем, что форма создания питомца принимает корректные данные.
        form = PetForm(data={
            'name': 'New Pet',
            'category': 'Домашнее',
            'family': 'Кошки',
            'breed': 'Сиамская',
            'gender': 'Мужской',
            'size': 'Средний',
            'arrival_date': '2023-01-02',
        })
        self.assertTrue(form.is_valid())
        
class ViewTests(TestCase):
    def setUp(self):
        # Создаем пользователя и объекты, которые будут использоваться в тестах.
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.shelter = Shelter.objects.create(name='Test Shelter', address='123 Test St', user=self.user)
        self.pet = Pet.objects.create(
            name='Test Pet',
            category='Домашнее',
            family='Кошки',
            breed='Сиамская',
            gender='Мужской',
            size='Средний',
            arrival_date='2023-01-01',
            shelter=self.shelter
        )
        # Создаем связь между пользователем и приютом
        UserShelter.objects.create(user=self.user, shelter=self.shelter)

    def test_index_view(self):
        # Проверяем, что главная страница возвращает корректный шаблон.
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_view(self):
        # Проверяем, что страница регистрации возвращает корректный шаблон.
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_login_view(self):
        # Проверяем, что страница входа возвращает корректный шаблон.
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_profile_view(self):
        # Проверяем, что страница профиля возвращает корректный шаблон.
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_shelter_list_view(self):
        # Проверяем, что страница со списком приютов возвращает корректный шаблон.
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('shelter_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shelter_list.html')

    def test_create_shelter_view(self):
        # Проверяем, что страница создания приюта возвращает корректный шаблон.
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('create_shelter'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_shelter.html')

    def test_shelter_detail_view(self):
        # Проверяем, что страница с деталями приюта возвращает корректный шаблон.
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('shelter_detail', args=[self.shelter.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shelter_detail.html')

    def test_create_pet_view(self):
        # Проверяем, что страница создания питомца возвращает корректный шаблон.
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('create_pet', args=[self.shelter.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_pet.html')

    def test_pet_detail_view(self):
        # Проверяем, что страница с деталями питомца возвращает корректный шаблон.
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('pet_detail', args=[self.pet.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pet_detail.html')