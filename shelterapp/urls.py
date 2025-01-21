from django.urls import path
from .views import register, user_login, shelter_list, create_shelter, edit_shelter, delete_shelter, CustomPasswordResetView, search_shelters, join_shelter, shelter_detail, create_pet, edit_pet

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('shelters/', shelter_list, name='shelter_list'),
    path('shelters/create/', create_shelter, name='create_shelter'),
    path('shelters/edit/<int:shelter_id>/', edit_shelter, name='edit_shelter'),
    path('shelters/delete/<int:shelter_id>/', delete_shelter, name='delete_shelter'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('shelters/search/', search_shelters, name='search_shelters'),
    path('shelters/join/<int:shelter_id>/', join_shelter, name='join_shelter'),
    path('shelters/<int:shelter_id>/', shelter_detail, name='shelter_detail'),
    path('shelters/<int:shelter_id>/create_pet/', create_pet, name='create_pet'),
    path('pets/<int:pet_id>/edit/', edit_pet, name='edit_pet'),
]