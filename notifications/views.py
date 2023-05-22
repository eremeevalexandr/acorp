from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import TicketNotification


def send_ticket_notification(request):
    # Логика отправки уведомления о заявке
    # Используйте модель TicketNotification для отслеживания отправленных уведомлений
    # Отправьте письмо по аналогии с сигналом send_ticket_notification

    return HttpResponse('Уведомление о заявке отправлено')


def send_comment_notification(request):
    # Логика отправки уведомления о комментарии
    # Используйте модель TicketNotification для отслеживания отправленных уведомлений
    # Отправьте письмо по аналогии с сигналом send_comment_notification

    return HttpResponse('Уведомление о комментарии отправлено')
