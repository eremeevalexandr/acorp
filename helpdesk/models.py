from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

User = get_user_model()


class Ticket(models.Model):
    """Модель для заявки"""

    class Status(models.TextChoices):
        OPEN = 'Open', 'Открыта'
        IN_PROGRESS = 'In Progress', 'В работе'
        RESOLVED = 'Resolved', 'Решена'
        CLOSED = 'Closed', 'Закрыта'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='пользователь')
    title = models.CharField('тема', max_length=200)
    description = models.TextField('описание')
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('дата изменения', auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OPEN,
        verbose_name='статус'
    )
    deadline = models.DateField('планируемая дата исполнения', null=True, blank=True)
    comment = models.ForeignKey(
        'helpdesk.Comment',
        null=True,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='комментарий'
    )

    def __str__(self):
        return self.title

    def get_comments(self):
        return self.comments.all()

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments', verbose_name='заявка')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', default=1)
    content = models.TextField('содержание комментария')
    created_at = models.DateTimeField('дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ['created_at']
        get_latest_by = 'ticket'

    def __str__(self):
        return f"Комментарий к заявке #{self.ticket.id}"

