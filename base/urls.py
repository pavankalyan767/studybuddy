from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('room/<str:id>/',views.room,name='room'),
    path('createRoom/',views.createRoom,name='createRoom'),
    path('updateRoom/<str:id>/',views.updateRoom,name='updateRoom'),
    path('deleteRoom/<str:id>',views.deleteRoom,name='deleteRoom'),
    path('deletemessage/<str:id>',views.deleteMessage,name='deletemessage'),
    path('profile/<str:id>/',views.userProfile,name='profile'),
]