from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict),
    path('prediction/',views.load_prediction),
]
