from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"), # Empty path means point to default page i.e. index
]
