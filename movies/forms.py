from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Movie
from django.forms import ModelForm


class UserForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2', ]


class Creation_form(ModelForm):
    class Meta:
        model = Movie

        fields = '__all__'

        exclude = ['user']
