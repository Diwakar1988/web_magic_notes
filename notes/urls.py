from django.urls import path

from . import views

urlpatterns = [
    # /notes/  ****** Empty path means point to default page i.e. index
    path('', views.index, name="index"),

    # /notes/note_id/ ex: /notes/1012/
    path('<int:note_id>/', views.details, name="details"),
]
