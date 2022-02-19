from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import null, true

# Create your models here.


class Club(models.Model):
    FACULTY = (
        ('Computing', 'Computing'),
        ('Networking', 'Networking'),
        ('Multimedia', 'Multimedia'),
    )
    name = models.CharField(max_length=50, null=True)
    faculty = models.CharField(max_length=50, null=True, choices=FACULTY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    yearChoices = (
        ('Year 1', 'Year 1'),
        ('Year 2', 'Year 2'),
        ('Year 3', 'Year 3'),
        ('Graduated', 'Graduated'),
    )
    TITLE = (
        ('President', 'President'),
        ('Advisor', 'Advisor'),
        ('Vice President', 'Vice President'),
        ('Event Manager', 'Event Manager'),
        ('Treasurer', 'Treasurer'),
        ('Founding Member', 'Founding Member'),
        ('Core Member', 'Core Member'),
        ('General Member', 'General Member'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    FACULTY = (
        ('Computing', 'Computing'),
        ('Networking', 'Networking'),
        ('Multimedia', 'Multimedia'),
    )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=20, null=True, choices=GENDER)
    phone = models.CharField(max_length=20, null=True)
    club = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=40, null=True, choices=TITLE)
    specialisation = models.CharField(
        max_length=20, null=True, choices=FACULTY)
    collegeEmail = models.CharField(max_length=50, null=True)
    personalEmail = models.CharField(max_length=50, null=True)
    year = models.CharField(max_length=10, null=True, choices=yearChoices)
    profile_pic = models.ImageField(
        default="default_profile.jpg",  null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class President(models.Model):
    yearChoices = (
        ('Year 1', 'Year 1'),
        ('Year 2', 'Year 2'),
        ('Year 3', 'Year 3'),
        ('Graduated', 'Graduated'),
    )
    name = models.CharField(max_length=50, null=True)
    club_name = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=20, null=True)
    collegeEmail = models.CharField(max_length=50, null=True)
    personalEmail = models.CharField(max_length=50, null=True)
    year = models.CharField(max_length=10, null=True, choices=yearChoices)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    FACULTY = (
        ('Computing', 'Computing'),
        ('Networking', 'Networking'),
        ('Multimedia', 'Multimedia'),
    )
    name = models.CharField(max_length=50, null=True)
    club = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL)
    faculty = models.CharField(max_length=50, null=True, choices=FACULTY)
    timing = models.TimeField(max_length=30, null=True)
    date = models.DateField(max_length=30, null=True)
    venue = models.CharField(max_length=50, null=True)
    event_manager = models.ForeignKey(
        Member, null=False, on_delete=models.SET_NULL),
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
