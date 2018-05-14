from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^session_word',views.index),
    url(r'^process',views.process),
    url(r'^reset',views.reset)
]