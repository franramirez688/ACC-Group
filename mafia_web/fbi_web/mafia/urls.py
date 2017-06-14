from django.conf.urls import url

from . import views, api_v1

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^v1/mafia_member', api_v1.index, name='index'),
]
