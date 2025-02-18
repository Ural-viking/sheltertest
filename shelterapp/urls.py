from django.urls import path
from .views import index, register, user_login,user_logout, profile, shelter_list, create_shelter, edit_shelter, delete_shelter, CustomPasswordResetView, search_shelters, join_shelter, shelter_detail, access_denied, create_pet, edit_pet, pet_detail, add_vet_assignment, edit_vet_assignment, vet_assignment_detail, admin_delete_shelter

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('shelters/', shelter_list, name='shelter_list'),
    path('shelters/create/', create_shelter, name='create_shelter'),
    path('shelters/<int:shelter_id>/edit/', edit_shelter, name='edit_shelter'),
    path('shelters/<int:shelter_id>/delete/', delete_shelter, name='delete_shelter'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('shelters/search/', search_shelters, name='search_shelters'),
    path('shelters/<int:shelter_id>/join/', join_shelter, name='join_shelter'),
    path('shelters/<int:shelter_id>/', shelter_detail, name='shelter_detail'),
    path('shelters/<int:shelter_id>/create_pet/', create_pet, name='create_pet'),
    path('pets/<int:pet_id>/edit/', edit_pet, name='edit_pet'),
    path('pets/<int:pet_id>/', pet_detail, name='pet_detail'),
    path('pets/<int:pet_id>/add_vet_assignment/', add_vet_assignment, name='add_vet_assignment'),
    path('pets/<int:pet_id>/edit_vet_assignment/<int:assignment_id>/', edit_vet_assignment, name='edit_vet_assignment'),
    path('pets/<int:pet_id>/vet_assignment/<int:assignment_id>/', vet_assignment_detail, name='vet_assignment_detail'),
    path('admin-delete-shelter/<int:shelter_id>/', admin_delete_shelter, name='admin_delete_shelter'),
    path('access_denied/', access_denied, name='access_denied'),
    
]