from django.urls import path;

# Views
from . import views;

urlpatterns = [
    path('', views.voters, name="Voters list")
];
