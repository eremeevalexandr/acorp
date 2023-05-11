from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'created_at', 'status', 'deadline', 'updated_at']
    list_filter = ['user']
