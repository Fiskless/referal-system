from django.contrib import admin
from .models import CustomUser, RelatedUsers


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(RelatedUsers)
class RelatedUsersAdmin(admin.ModelAdmin):
    pass
