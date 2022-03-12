import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class MemberFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    # end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Member
        fields = ['name']
        # exclude = ['date_created', 'profile_pic',
        #            'user', 'gender', 'personalEmail', 'Year', 'Phone', 'specialisation']


class EventFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    # end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['name', 'club']
        # exclude = ['date_created']
