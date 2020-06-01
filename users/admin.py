from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# admin.site.register(models.User, CustomUserAdmin)


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "birthdate",
                    "bio",
                    "language",
                    "currency",
                )
            },
        ),
    )
