from django.urls import path
from . import views

app_name = 'helpdesk'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('<int:ticket_id>/', views.view_ticket, name='view_ticket'),
    path('ticket/<int:ticket_id>/complete/', views.complete_ticket, name='complete_ticket'),
    path('ticket/<int:ticket_id>/reopen/', views.reopen_ticket, name='reopen_ticket'),
]
