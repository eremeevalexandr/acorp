from django.contrib import admin
from django.utils.html import format_html
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'created_at', 'status', 'deadline', 'updated_at']
    list_filter = ['status', 'user', 'created_at', 'updated_at', 'deadline']

