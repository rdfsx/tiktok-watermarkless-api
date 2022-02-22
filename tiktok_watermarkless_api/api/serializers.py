from rest_framework import serializers

from tiktok_watermarkless_api.api.models import MediaResult


class MediaResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaResult
        fields = ['title', 'author', 'link']
