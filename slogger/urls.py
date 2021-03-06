"""slogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from api import views as api
from web import views as web

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # API-TOKEN
    url(r'^api/addLogDefault/$', api.addDefaultLog),

    # API-WEB
    url(r'^api/log/default/(?P<id>[0-9]+)/$', api.appDefaultLogs),

    # WEB
    url(r'^web/$', web.home),
    url(r'^web/login/$', web.home),
    url(r'^web/logout/$', web.logout_view),
    url(r'^web/applist/$', web.applist),
    url(r'^web/defaultlog/(?P<id>[0-9]+)/$', web.defaultlog),
    url(r'^web/addapp/$', web.addapp),

]
