from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password1', 'password2', 'is_teacher', 'is_teacher',)
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff',)
        })
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_teacher', 'password',)
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff',)
        })
    )
    list_display = ['email', 'username', 'is_student', 'is_teacher', ]
    searchfields = ('email', 'username',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)


admin.site.unregister(Group)
