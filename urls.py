from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^djaton/', include('djaton.urls')),
    url(r'^admin/', admin.site.urls),
]
