from django.contrib import admin
from .models import Basic

class NoDeleteAdminmixin:
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Basic)
class BasicAdmin(NoDeleteAdminmixin, admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Basic.objects.exists()

