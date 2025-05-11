from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('settings/', views.settings_view, name='settings'),
    path('settings/password/', views.password_change, name='password_change'),
] 