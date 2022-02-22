from rest_framework.response import Response
from rest_framework.views import APIView

from tiktok_watermarkless_api.api.mixins import MainTikTokMediaMixin
from tiktok_watermarkless_api.api.permissions import IsAllowed


class MediaView(APIView, MainTikTokMediaMixin):
    permission_classes = [IsAllowed]

    def get(self, request, link):
        media = self.get_info(link)
        return Response(media)
