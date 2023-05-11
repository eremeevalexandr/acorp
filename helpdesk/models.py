from django.db import models
from django.contrib.auth.models import User

from accounts.models import CustomUser


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
        default=Status.OPEN
    )
    deadline = models.DateField('планируемая дата исполнения', null=True, blank=True)

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'
