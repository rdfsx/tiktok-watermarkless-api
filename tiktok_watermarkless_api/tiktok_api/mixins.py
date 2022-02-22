import time
from abc import ABC, abstractmethod
from typing import Optional

from rest_framework import serializers
from yt_dlp import YoutubeDL


class AbstractMediaMixin(ABC):

    @abstractmethod
    def get_info(self, link: str) -> Optional[serializers.Serializer]:
        pass


class TikTokMixin(AbstractMediaMixin):
    """
    Class for working with tik-tok. Make changes to it, not to the view
    """
    def get_info(self, link: str) -> Optional[dict]:
        if result := MainTikTokMediaMixin().get_info(link):
            return result
        return None


class MainTikTokMediaMixin(AbstractMediaMixin):

    def get_info(self, link: str) -> Optional[dict]:
        ydl_opts = {
            'quiet': True,
            "skip_download": True,
        }
        downloader = YoutubeDL(ydl_opts)
        info: dict = downloader.extract_info(link)
        if info:
            return info
        return None
