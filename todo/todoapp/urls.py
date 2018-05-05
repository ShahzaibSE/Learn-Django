from django.urls import path;

# Views
from . import views;

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # todo
    path('addtodo/', views.tododetail, name='tododetail')
]