#!/usr/bin/env python
#coding: utf-8
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
        path('polls/', include('polls.urls')),
        path('admin/', admin.site.urls),
        ]
