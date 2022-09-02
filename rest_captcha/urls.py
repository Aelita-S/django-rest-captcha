from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.RestCaptchaView.as_view(), name='rest_captcha'),
]
