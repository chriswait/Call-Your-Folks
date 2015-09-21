from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^log_call$', views.log_call, name='log_call'),
    url(r'^delete_call$', views.delete_call, name='delete_call'),
    url(r'^recommended$', views.recommended, name='recommended'),
]
