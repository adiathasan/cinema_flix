from django.urls import path
from .views import *


urlpatterns = [
    path('', base, name='base'),
    path('User_account/', home_page, name='home_page'),
    path('create/', home_page, name='create'),
    path('edit/<str:pk>/', edit, name='edit'),
    path('delete/<str:movie_id>/', delete, name='delete'),
    path('login/', login_user, name='login'),
    path('logout/', logout_url, name='logout'),
    path('register/', register_user, name='register'),
]
