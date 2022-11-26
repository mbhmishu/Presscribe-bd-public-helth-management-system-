
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AccountApp.urls')),
    path('managment_app/', include('managment_app.urls')),
    path('prescribeapp/', include('prescribeapp.urls')),
    path('blogapp/', include('blogapp.urls')),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)