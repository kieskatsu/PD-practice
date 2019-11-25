from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, show_ranking, show_video, evaluate

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('ranking/', show_ranking, name='ranking'),
    path('judge/', show_video, name='judge'),
    path('evaluate/<slug:screen_name>', evaluate, name='evaluate')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
