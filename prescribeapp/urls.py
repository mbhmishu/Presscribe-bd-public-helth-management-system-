
from django.contrib import admin
from django.urls import path
from prescribeapp import views
app_name = 'prescrib'

urlpatterns = [
    path('patient_profile/<username>/', views.patient_profile, name='patient_profile'),
    
    
    
]
