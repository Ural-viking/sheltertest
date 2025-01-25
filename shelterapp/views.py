from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm, ShelterForm, CustomPasswordResetForm, PetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from .models import Shelter, UserShelter, Pet

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shelter_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# @login_required
# def shelter_list(request):
#     shelters = Shelter.objects.filter(user=request.user)
#     return render(request, 'shelter_list.html', {'shelters': shelters})

# @login_required
# def shelter_list(request):
#     shelters = Shelter.objects.filter(user=request.user)
#     print(f"Shelters for user {request.user}: {shelters}")  # Отладочное сообщение
#     return render(request, 'shelter_list.html', {'shelters': shelters})


@login_required
def shelter_list(request):
    user_shelters = UserShelter.objects.filter(user=request.user)
    shelters = [user_shelter.shelter for user_shelter in user_shelters]
    return render(request, 'shelter_list.html', {'shelters': shelters})

@login_required
def create_shelter(request):
    if request.method == 'POST':
        form = ShelterForm(request.POST, request.FILES)
        if form.is_valid():
            shelter = form.save(commit=False)
            shelter.user = request.user  # Устанавливаем текущего пользователя
            print(f"User set to: {shelter.user}")  # Отладочное сообщение
            shelter.save()
            UserShelter.objects.create(user=request.user, shelter=shelter)
            return redirect('shelter_list')  # Перенаправляем на страницу списка приютов
        else:
            print(f"Form errors: {form.errors}")  # Отладочное сообщение
    else:
        form = ShelterForm()
    return render(request, 'create_shelter.html', {'form': form})

@login_required
def shelter_detail(request, shelter_id):
    shelter = get_object_or_404(Shelter, id=shelter_id)
    if not request.user.is_superuser and not UserShelter.objects.filter(shelter=shelter, user=request.user).exists():
        return render(request, 'access_denied.html')
    return render(request, 'shelter_detail.html', {'shelter': shelter})

@login_required
def edit_shelter(request, shelter_id):
    shelter = get_object_or_404(Shelter, id=shelter_id)
    if not request.user.is_superuser and not UserShelter.objects.filter(shelter=shelter, user=request.user).exists():
        return render(request, 'access_denied.html')
    if request.method == 'POST':
        form = ShelterForm(request.POST, request.FILES, instance=shelter)
        if form.is_valid():
            form.save()
            return redirect('shelter_detail', shelter_id=shelter.id)
    else:
        form = ShelterForm(instance=shelter)
    return render(request, 'edit_shelter.html', {'form': form})

@login_required
def delete_shelter(request, shelter_id):
    shelter = get_object_or_404(Shelter, id=shelter_id)
    if not request.user.is_superuser and not UserShelter.objects.filter(shelter=shelter, user=request.user).exists():
        return render(request, 'access_denied.html')
    if request.method == 'POST':
        shelter.delete()
        return redirect('shelter_list')
    return render(request, 'delete_shelter.html', {'shelter': shelter})

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'password_reset.html'
    success_url = reverse_lazy('password_reset_done')
    
@login_required
def search_shelters(request):
    query = request.GET.get('q')
    shelters = Shelter.objects.all()
    if query:
        shelters = shelters.filter(name__icontains=query)
    user_shelters = UserShelter.objects.filter(user=request.user).values_list('shelter_id', flat=True)
    return render(request, 'search_shelters.html', {'shelters': shelters, 'query': query, 'user_shelters': user_shelters})

@login_required
def join_shelter(request, shelter_id):
    shelter = get_object_or_404(Shelter, id=shelter_id)
    if not UserShelter.objects.filter(user=request.user, shelter=shelter).exists():
        UserShelter.objects.create(user=request.user, shelter=shelter)
    return redirect('shelter_detail', shelter_id=shelter.id)

@login_required
def create_pet(request, shelter_id):
    shelter = get_object_or_404(Shelter, id=shelter_id)
    if not request.user.is_superuser and not UserShelter.objects.filter(shelter=shelter, user=request.user).exists():
        return render(request, 'access_denied.html')
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.shelter = shelter
            pet.save()
            return redirect('shelter_detail', shelter_id=shelter.id)
    else:
        form = PetForm()
    return render(request, 'create_pet.html', {'form': form})

@login_required
def edit_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if not request.user.is_superuser and not UserShelter.objects.filter(shelter=pet.shelter, user=request.user).exists():
        return render(request, 'access_denied.html')
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('shelter_detail', shelter_id=pet.shelter.id)
    else:
        form = PetForm(instance=pet)
    return render(request, 'edit_pet.html', {'form': form})

def access_denied(request):
    return render(request, 'access_denied.html')