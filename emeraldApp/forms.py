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


class MemberProfileForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['user']
        # GENDER_CHOICES = (
        #     ('Male', 'Male'),
        #     ('Female', 'Female'),
        #     ('Other', 'Other')
        # )
        # gender_field = forms.ChoiceField(choices=GENDER_CHOICES)
        # tailwindClass = "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': tailwindClass}),
        #     'gender': forms.TextInput(attrs={'class': tailwindClass}),
        #     'phone': forms.TextInput(attrs={'class': tailwindClass}),
        #     'club': forms.TextInput(attrs={'class': tailwindClass}),
        #     'title': forms.TextInput(attrs={'class': tailwindClass}),
        #     'specialisation': forms.TextInput(attrs={'class': tailwindClass}),
        #     'collegeEmail': forms.TextInput(attrs={'class': tailwindClass}),
        #     'personalEmail': forms.TextInput(attrs={'class': tailwindClass}),
        #     'year': forms.TextInput(attrs={'class': tailwindClass})
        # }

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"}),
            'phone': forms.TextInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'collegeEmail': forms.EmailInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none'}),
            'personalEmail': forms.EmailInput(attrs={'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none'}),

        }


class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
