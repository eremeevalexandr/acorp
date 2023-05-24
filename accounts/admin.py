from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'first_name', 'phone_number', 'get_staff_status']
    search_fields = ['username', 'last_name', 'first_name', 'phone_number']

    def get_staff_status(self, obj):
        if obj.is_staff:
            return "Персонал"
        else:
            return ""
    get_staff_status.short_description = 'Админка'
