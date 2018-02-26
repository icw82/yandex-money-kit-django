# -*- coding: utf-8 -*-

from django.urls import path

from .views import NoticeFormView
from .views import CheckOrderFormView


urlpatterns = [
    path('^check/',
        CheckOrderFormView.as_view(),
        name='yandex_money_check'),

    path('^aviso/',
        NoticeFormView.as_view(),
        name='yandex_money_notice'),
]
