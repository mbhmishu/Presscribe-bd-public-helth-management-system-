from django.urls import path
from . import views

urlpatterns = [
    path('verify_acount/<username>/', views.verify_acount, name='verify_acount'),
    path('unverify_acount/<username>/', views.unverify_acount, name='unverify_acount'),
    
    
]
