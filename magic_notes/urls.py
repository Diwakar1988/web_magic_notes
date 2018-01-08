from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notes.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'accounts/logged_out.html'}, name='logout'),
]
