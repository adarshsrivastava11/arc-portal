from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from portal.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/$', index),
    url(r'^api/signup/$', signup),
    # url(r'^(?P<path>.*)$', serve, {'document_root':'../app_frontend'}),
]
