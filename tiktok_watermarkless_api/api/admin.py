from django.contrib import admin

from tiktok_watermarkless_api.api.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
