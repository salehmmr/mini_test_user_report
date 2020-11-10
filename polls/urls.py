from django.conf.urls import url, include
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
]
