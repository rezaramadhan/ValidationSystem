from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.validation_form, name='validation_form'),
    url(r'token$', views.validation_form, name='code_verification')
]
