from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("check_num", views.check_num),
    path('restart', views.restart),
]