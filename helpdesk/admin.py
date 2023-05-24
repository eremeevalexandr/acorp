from django.contrib import admin
from django.forms import HiddenInput
from .models import Ticket, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = []

    def get_formset(self, request, obj=None, **kwargs):
        # Вызываем родительский метод для получения формсета
        formset = super().get_formset(request, obj, **kwargs)
        # Проверяем, является ли пользователь суперпользователем
        if not request.user.is_superuser:
            # Устанавливаем текущего пользователя в качестве значения по умолчанию для поля 'user'
            formset.form.base_fields['user'].initial = request.user
            # Делаем поле 'user' только для чтения, чтобы пользователь не мог его изменить
            formset.form.base_fields['user'].widget.attrs['readonly'] = True
            # Отключаем возможность добавлять, изменять или удалять связанные объекты в поле 'user'
            formset.form.base_fields['user'].widget.can_add_related = False
            formset.form.base_fields['user'].widget.can_change_related = False
            formset.form.base_fields['user'].widget.can_delete_related = False
            # Используем виджет HiddenInput, чтобы поле 'user' было скрыто
            formset.form.base_fields['user'].widget = HiddenInput()
        return formset


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'created_at', 'status', 'deadline', 'updated_at', 'id']
    list_filter = ['status', 'user', 'created_at', 'updated_at', 'deadline']
    search_fields = ['id', 'user__last_name', 'user__first_name']
    inlines = [CommentInline]
    exclude = ['comment']
