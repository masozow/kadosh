from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

from .urls import urlpatterns as base_urlpatterns

# Sirve las imágenes subidas (MEDIA_ROOT) aunque DEBUG sea False.
# Suficiente para una demo; en un hosting real usa nginx para esto.
urlpatterns = list(base_urlpatterns) + [
    url(r'^archivos/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
