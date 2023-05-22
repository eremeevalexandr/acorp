from django.contrib import admin
from .models import Ticket, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'created_at', 'status', 'deadline', 'updated_at']
    list_filter = ['status', 'user', 'created_at', 'updated_at', 'deadline']
    inlines = [CommentInline]
