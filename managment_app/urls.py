from django.urls import path
from . import views

app_name='managementapp'

urlpatterns = [
    path('verify_acount/<username>/', views.verify_acount, name='verify_acount'),
    path('unverify_acount/<username>/', views.unverify_acount, name='unverify_acount'),
    path('verify_author/', views.verify_author, name='verify_author'),
    
    
]
