from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('clubs/', views.clubs, name="clubs"),
    path('member_profile/<str:pk_test>',
         views.memberProfile, name='member_profile'),
    path('members/', views.member, name="members"),
    path('events/', views.events, name="events"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user"),

    path('view_members/<str:pk>',
         views.viewMembers, name="view_members"),

    # Paths for Event CRUD
    path('create_event/', views.createEvent, name="create_event"),
    path('update_event/<str:pk>', views.updateEvent, name="update_event"),
    path('delete_event/<str:pk>', views.deleteEvent, name="delete_event"),

    # Paths for Member CRUD
    path('create_member/', views.createMember, name="create_member"),
    path('update_member/<str:pk>', views.updateMember, name="update_member"),
    path('delete_member/<str:pk>', views.deleteMember, name="delete_member"),

    # Paths for Club CRUD
    path('create_club/', views.createClub, name="create_club"),
    path('update_club/<str:pk>', views.updateClub, name="update_club"),
    path('delete_club/<str:pk>', views.deleteClub, name="delete_club"),

    # path('logout/', views.logoutUser, name="logout"),
]
