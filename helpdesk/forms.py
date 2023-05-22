from django import forms
from .models import Ticket, Comment


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Содержание комментария'
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4})
        }
