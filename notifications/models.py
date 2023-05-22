from django.db import models
from helpdesk.models import Ticket


class TicketNotification(models.Model):
    ticket = models.ForeignKey('helpdesk.Ticket', on_delete=models.CASCADE, related_name='notifications',
                               verbose_name='заявка')
    recipient_email = models.EmailField()
    notification_type = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'уведомление о заявке'
        verbose_name_plural = 'уведомления о заявках'
