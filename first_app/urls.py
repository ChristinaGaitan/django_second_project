from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_user', views.new_user, name='new_user'),
    path('users', views.users, name='users'),
]
