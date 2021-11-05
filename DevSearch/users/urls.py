from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('', views.profiles, name='profiles'),
    path('userprofile/<str:pk>/', views.userprofile, name='userprofile'),
    path('account/', views.userAccount, name='account'),
    path('editaccount/', views.editAccount, name='edit-account'),
    path('createskill/', views.createSkill, name='createskill'),
    path('updateskill/<str:pk>/', views.updateSkill, name='updateskill'),
    path('deleteskill/<str:pk>/', views.deleteSkill, name='deleteskill')
]
