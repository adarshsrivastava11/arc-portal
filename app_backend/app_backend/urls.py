from django.conf.urls import url
from django.contrib import admin
from portal.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
]
