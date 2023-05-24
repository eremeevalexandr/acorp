from django.db.models.signals import post_save
from django.dispatch import receiver
from helpdesk.models import Ticket, Comment
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from config_app.email_setting import POST_MAIL


@receiver(post_save, sender=Ticket)
def send_ticket_notification(sender, instance, created, **kwargs):
    if created:
        notification_type = 'новая заявка создана'
    else:
        notification_type = 'заявка изменена'

    recipient_email = [instance.user.email]  # Передаем email как список с одним элементом
    recipient_list = recipient_email + POST_MAIL  # Объединяем recipient_email и POST_MAIL
    subject = f'Уведомление о заявке #{instance.id}'
    html_message = render_to_string('notifications/ticket_notification.html',
                                    {
                                        'ticket': instance,
                                        'notification_type': notification_type
                                    }
                                    )
    plain_message = strip_tags(html_message)
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        html_message=html_message
    )


@receiver(post_save, sender=Comment)
def send_comment_notification(sender, instance, created, **kwargs):
    if created:
        ticket = instance.ticket
        recipient_email = [ticket.user.email]   # Передаем email как список с одним элементом
        recipient_list = recipient_email + POST_MAIL    # Объединяем recipient_email и POST_MAIL
        subject = f'Уведомление о комментарии к заявке #{ticket.id}'
        html_message = render_to_string('notifications/comment_notification.html',
                                        {'comment': instance, 'ticket': ticket})
        plain_message = strip_tags(html_message)
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            html_message=html_message
        )
