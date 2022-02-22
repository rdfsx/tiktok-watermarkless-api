from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('video/<str:link>', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
