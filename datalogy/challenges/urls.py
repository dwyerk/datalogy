from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/', views.create, name='create'),
    url(r'^([a-zA-Z0-9\-]+)/edit', views.edit, name='edit'),
    url(r'^([a-zA-Z0-9\-]+)/', views.details, name='details')
]
