"""
URLs de la aplicación Chatbot.
"""

from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send_message, name='send_message'),
    path('info/', views.get_bot_info, name='bot_info'),
]
