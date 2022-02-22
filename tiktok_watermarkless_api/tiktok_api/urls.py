from django.urls import re_path

from tiktok_watermarkless_api.tiktok_api import views

app_name = "tiktok_api"

urlpatterns = [
    re_path(r'^(?P<link>[ -~]+)', views.TikTokView.as_view(), name='tiktok_api'),
]
