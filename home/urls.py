from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.NewTask.as_view(),name="homeView"),
    path('deleteTask', views.deleteTask,name="deleteTask"),
]