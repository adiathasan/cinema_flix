from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home_page'),
    path('create/', create, name='create'),
    path('edit/<str:movie_id>', edit, name='edit'),
    path('delete/<str:movie_id>', delete, name='delete'),
    path('login/', login_user, name='login'),
    path('logout/', logout_url, name='logout'),
    path('register/', register_user, name='register'),
]
