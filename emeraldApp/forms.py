from django.forms import ModelForm
from .models import *


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
