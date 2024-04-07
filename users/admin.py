from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {"fields": ("username", "password")}),
        ("Information", {"fields": ("first_name", "last_name", "email")}),
        ("Add field", {"fields": ("profile_image", "short_description")}),
        (
            "right",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        ("important action", {"fields": ("last_login", "date_joined")}),
    ]