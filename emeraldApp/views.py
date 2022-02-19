from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import Group

from emeraldApp.decorators import unauthenticated_user
from .models import *
from .forms import *
from .filters import MemberFilter, EventFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import *


@login_required(login_url='login')
@admin_only
def home(request):
    return render(request, 'emeraldApp/dashboard.html')


@login_required(login_url='login')
def clubs(request):
    clubs = Club.objects.all()
    total_clubs = clubs.count()
    context = {'clubs': clubs, 'total_clubs': total_clubs}
    return render(request, 'emeraldApp/clubs.html', context)


@login_required(login_url='login')
def member(request):
    members = Member.objects.all()
    total_members = members.count
    ()
    # Total number of IWDC members
    total_IWDC_members = members.filter(
        club__name__contains='Islington Web Development Club')
    # Total number of CyberOps members
    total_CyberOps_members = members.filter(
        club__name__contains='CyberOps Club').count()
    # Total number of CyberDefenders members
    total_CyberDefenders_members = members.filter(
        club__name__contains='Cyber Defenders Club').count()

    myFilter = MemberFilter(request.GET, queryset=members)
    members = myFilter.qs

    context = {'members': members, 'total_members': total_members,
               'total_IWDC_members': total_IWDC_members, 'total_CyberOps_members': total_CyberOps_members, 'total_CyberDefenders_members': total_CyberDefenders_members, 'customer': member, 'myFilter': myFilter}
    return render(request, 'emeraldApp/members.html', context)


@login_required(login_url='login')
def events(request):
    events = Event.objects.all()
    myFilter = EventFilter(request.GET, queryset=events)
    events = myFilter.qs
    return render(request, 'emeraldApp/events.html', {'events': events, 'myFilter': myFilter})


@login_required(login_url='login')
def memberProfile(request, pk_test):
    member = Member.objects.get(id=pk_test)

    context = {'member': member}
    return render(request, 'emeraldApp/memberProfile.html', context)


@login_required(login_url='login')
def clubProfile(request, pk_test):
    club = Club.objects.get(id=pk_test)

    context = {'club': club}
    return render(request, 'emeraldApp/club_profile.html', context)

# Functions for Event CRUD


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createEvent(request):
    form = EventForm()

    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/events')
    context = {'form': form}
    return render(request, 'emeraldApp/form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateEvent(request, pk):

    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)

    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/events')
    context = {'form': form}
    return render(request, 'emeraldApp/form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == "POST":
        event.delete()
        return redirect('/members')
    context = {'item': event}
    return render(request, 'emeraldApp/delete_event.html', context)

# Functions for Member CRUD


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createMember(request):
    form = MemberForm()

    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/members')
    context = {'form': form}
    return render(request, 'emeraldApp/form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateMember(request, pk):

    member = Member.objects.get(id=pk)
    form = MemberForm(instance=member)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/members')
    context = {'form': form}
    return render(request, 'emeraldApp/form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteMember(request, pk):
    member = Member.objects.get(id=pk)
    if request.method == "POST":
        member.delete()
        return redirect('/members')
    context = {'item': member}
    return render(request, 'emeraldApp/delete_member.html', context)

# Functions for Club CRUD


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createClub(request):
    form = ClubForm()

    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clubs')
    context = {'form': form}
    return render(request, 'emeraldApp/form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateClub(request, pk):

    club = Club.objects.get(id=pk)
    form = ClubForm(instance=club)

    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect('/clubs')
    context = {'form': form}
    return render(request, 'emeraldApp/form.html', context)


@login_required(login_url='login')
def viewMembers(request, pk):
    club = Club.objects.get(id=pk)

    context = {'club': club}
    return render(request, 'emeraldApp/IWDC_members.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteClub(request, pk):
    club = Club.objects.get(id=pk)
    if request.method == "POST":
        club.delete()
        return redirect('/clubs')
    context = {'item': club}
    return render(request, 'emeraldApp/delete_club.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['member', 'superuser'])
def accountSettings(request):
    member = request.user.member
    form = MemberProfileForm(instance=member)

    if request.method == "POST":
        form = MemberProfileForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'emeraldApp/account_settings.html', context)

# Register and Login functions


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='member')
            user.groups.add(group)
            Member.objects.create(
                user=user,
                name=user.username
            )

            messages.success(
                request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'emeraldApp/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'emeraldApp/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def userPage(request):
    context = {}
    return render(request, 'emeraldApp/user.html', context)
