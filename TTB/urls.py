from django.urls import path
from .views import *
from . import views

app_name='TTB'

urlpatterns = [
    path('', Homm, name='Homm'),
    path('', Home, name='Home'),
    path('Form1A', Form1A, name='Form1A'),
    path('Form1B', Form1B, name='Form1B'),
    path('Form2A', Form2A, name='Form2A'),
    path('Form2B', Form2B, name='Form2B'),
    path('Form3A', Form3A, name='Form3A'),
    path('Form3B', Form3B, name='Form3B'),
    path('Form4A', Form4A, name='Form4A'),
    path('Form4B', Form4B, name='Form4B'),
]