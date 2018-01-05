from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authorize/', include('authorize.urls')),
    path('notes/', include('notes.urls')),
]
