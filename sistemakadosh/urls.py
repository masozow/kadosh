from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'sistemakadosh.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('kadoshapp.urls')),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #                    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #comentar esto cuando Debug=False
