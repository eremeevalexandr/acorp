from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']
        labels = {'title': 'Заголовок', 'description': 'Описание'}


class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status']
        labels = {'title': 'Заголовок', 'description': 'Описание', 'status': 'Статус'}
        widgets = {'status': forms.Select(choices=Ticket.Status)}
