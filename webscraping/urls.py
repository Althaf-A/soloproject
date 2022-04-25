"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login,name="Login"),
    path('Register/',views.Register,name="Register"),
    path('admin_dashboard/', views.admin_dashboard , name='admin_dashboard'),
    path('admin_new_worker_aprove/', views.admin_new_worker_aprove, name='admin_new_worker_aprove'),
    path('admin_users_details/', views.admin_users_details, name='admin_users_details'),
    path('admin_user_profile_view/', views.admin_user_profile_view, name='admin_user_profile_view'),
    path('admin_worker_profile_view/', views.admin_worker_profile_view, name='admin_worker_profile_view'),
    path('admin_workers_details/', views.admin_workers_details, name='admin_workers_details'),
    path('admin_workers_register/', views.admin_workers_register, name='admin_workers_register'),
    path('admin_user_activity/', views.admin_user_activity, name='admin_user_activity'),
    path('admin_feedback_cards/', views.admin_feedback_cards, name='admin_feedback_cards'),
    path('admin_workers_feedbacks/', views.admin_workers_feedbacks, name='admin_workers_feedbacks'),
    path('admin_users_feedbacks/', views.admin_users_feedbacks, name='admin_users_feedbacks'),

    #############################user##########################

    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user_search_worker/', views.user_search_worker, name='user_search_worker'),
    path('user_worker_profile/', views.user_worker_profile, name='user_worker_profile'),
    path('user_worker_reports/', views.user_worker_reports, name='user_worker_reports'),
    path('user_history_list/', views.user_history_list, name='user_history_list'),

]
