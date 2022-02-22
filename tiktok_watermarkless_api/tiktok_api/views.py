from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from yt_dlp.utils import DownloadError

from tiktok_watermarkless_api.tiktok_api.mixins import TikTokMixin
from tiktok_watermarkless_api.tiktok_api.serializers import MainTikTokResultSerializer


@api_view(['GET'])
def api_root(request):
    return Response({
        'tiktok_api': reverse('tiktok_api', request=request),
    })


class TikTokView(APIView, TikTokMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, link):
        try:
            media_info = self.get_info(link)
        except DownloadError:
            return Response({"error": "Download Error"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = MainTikTokResultSerializer(data=media_info)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
