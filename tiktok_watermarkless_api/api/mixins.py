from abc import ABC, abstractmethod

from yt_dlp import YoutubeDL

from tiktok_watermarkless_api.api.models import MediaResult


class AbstractMediaMixin(ABC):

    @abstractmethod
    def get_info(self, link: str) -> MediaResult:
        pass


class MainTikTokMediaMixin(AbstractMediaMixin):

    def get_info(self, link: str) -> MediaResult:
        ydl_opts = {
            "skip_download": True,
        }
        downloader = YoutubeDL(ydl_opts)
        info = downloader.extract_info(link)
        return MediaResult(**info)
