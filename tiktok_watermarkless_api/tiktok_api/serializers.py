from rest_framework import serializers


class MainTikTokResultSerializer(serializers.Serializer):
    title = serializers.CharField()
    uploader = serializers.CharField(default=None)
    url = serializers.URLField(default=None)
