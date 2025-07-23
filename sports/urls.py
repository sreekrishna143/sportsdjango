from django.urls import path
from .import views
urlpatterns=[
path('',views.function1, name="index"),
path('index',views.function6, name="home"),
path('matches/',views.function2, name="matches"),
path('players/',views.player_list, name="players"),
path('blog/',views.function4, name="blog"),
path('contact/',views.function5, name="contact"),
path('sign/',views.function7, name="sign"),
path('login/',views.login, name="login"),
path('register/', views.register, name="register"),
path('profile/', views.profile, name="profile"),
path('feedbackpagecall/', views.feedbackpagecall, name='feedbackpagecall'),
path('feedbacklogic/', views.feedbacklogic, name='feedbacklogic'),
path('ticketbookingpagecall/', views.ticketbookingpagecall, name='ticketbookingpagecall'),
path('logout/', views.logout, name="logout"),
path('add/', views.add_player, name='add_player'),
]