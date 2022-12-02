
from django.contrib import admin
from django.urls import path
from prescribeapp import views
app_name = 'prescrib'

urlpatterns = [
    path('patient_profile/<username>/', views.patient_profile, name='patient_profile'),
    path('Add_to_patientprofile/<username>/', views.Add_to_patientprofile, name='Add_to_patientprofile'),
    path('prescrition_detail/<pk>/', views.prescrition_detail, name='prescrition_detail'),
    
    
    
]
