from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('send_ticket_notification/', views.send_ticket_notification, name='send_ticket_notification'),
    path('send_comment_notification/', views.send_comment_notification, name='send_comment_notification'),
]
