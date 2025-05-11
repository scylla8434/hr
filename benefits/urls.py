from django.urls import path
from . import views

app_name = 'benefits'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # Benefit Plans
    path('plans/', views.plan_list, name='plan_list'),
    path('plans/create/', views.plan_create, name='plan_create'),
    path('plans/<int:pk>/', views.plan_detail, name='plan_detail'),
    path('plans/<int:pk>/edit/', views.plan_edit, name='plan_edit'),
    path('plans/<int:pk>/delete/', views.plan_delete, name='plan_delete'),
    
    # Enrollments
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollments/create/', views.enrollment_create, name='enrollment_create'),
    path('enrollments/<int:pk>/', views.enrollment_detail, name='enrollment_detail'),
    path('enrollments/<int:pk>/edit/', views.enrollment_edit, name='enrollment_edit'),
    path('enrollments/<int:pk>/delete/', views.enrollment_delete, name='enrollment_delete'),
    
    # Wellness Programs
    path('wellness/', views.wellness_list, name='wellness_list'),
    path('wellness/create/', views.wellness_create, name='wellness_create'),
    path('wellness/<int:pk>/', views.wellness_detail, name='wellness_detail'),
    path('wellness/<int:pk>/edit/', views.wellness_edit, name='wellness_edit'),
    path('wellness/<int:pk>/delete/', views.wellness_delete, name='wellness_delete'),
    
    # Wellness Activities
    path('wellness/activities/', views.activity_list, name='activity_list'),
    path('wellness/activities/create/', views.activity_create, name='activity_create'),
    path('wellness/activities/<int:pk>/', views.activity_detail, name='activity_detail'),
    path('wellness/activities/<int:pk>/edit/', views.activity_edit, name='activity_edit'),
    path('wellness/activities/<int:pk>/delete/', views.activity_delete, name='activity_delete'),
    
    # Wellness Participation
    path('wellness/participation/', views.participation_list, name='participation_list'),
    path('wellness/participation/create/', views.participation_create, name='participation_create'),
    path('wellness/participation/<int:pk>/', views.participation_detail, name='participation_detail'),
    path('wellness/participation/<int:pk>/edit/', views.participation_edit, name='participation_edit'),
    path('wellness/participation/<int:pk>/delete/', views.participation_delete, name='participation_delete'),
] 