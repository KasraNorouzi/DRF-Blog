from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

app_name = 'accounts'


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser', 'is_active')
    list_filter = ('is_superuser', 'is_active', 'email')
    search_fields = ('email', 'is_superuser')
    ordering = ('email',)
    fieldsets = (
        ('authentication', {
            'fields':
                ('email', 'password')
        }),
        ('permissions', {
            'fields':
                ('is_staff', 'is_superuser', 'is_active')
        }),
        ('group_permissions', {
            'fields':
                ('groups', 'user_permissions')
        }),
        ('important_date', {
            'fields':
                ('last_login',)
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", 'password2', "is_superuser", "is_active", 'is_staff'
            )}
         ),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
