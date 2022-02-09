from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.contrib.auth.models import User


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
