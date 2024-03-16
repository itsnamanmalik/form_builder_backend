from django.contrib import admin
from django.urls import path, include
from common import views

urlpatterns = [
    path('create-random/<int:count>',views.CreateRandomUserView.as_view()),
]
