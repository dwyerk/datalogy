"""datalogy URL Configuration"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/challenges/', permanent=False)),
    url(r'^challenges/', include('challenges.urls', namespace='challenges')),
    url(r'^users/', include('users.urls', namespace='users'))
]
