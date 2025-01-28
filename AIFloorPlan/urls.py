"""
Definition of urls for AIFloorPlan.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
      path('generate-floor-plan/', views.generate_floor_plan, name='generate_floor_plan'),
 
   
   
]
