from django.urls import path

from sample_app import views

urlpatterns = [
    path('last_points', views.last_points, name='last_points'),
]
