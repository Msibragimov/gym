from django.urls import path

from apps.paper import views

urlpatterns = [
    path('', views.home, name='homepage'),
]