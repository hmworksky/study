#coding:UTF-8
"""testdj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
admin.autodiscover()
from testdj1 import view
from testdj1 import tools
#from sign.views import index
from blog.views import *
from django.conf.urls import url,include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',view.hello),
    #url(r'^$',view.hh),
    url(r'^hellodate/(\d{1,2})/$',view.hellodate),
    url(r'^template/$',view.current_html),
    url(r'^template/nav/$',view.current_nav),
    url(r'^return/$',view.return_interface),
    url(r'^login_action/$',view.login_action),
    url(r'^management/$',view.management),
    url(r'^tools/$',tools.bejson),
    url(r'^results/$',tools.results),
    url(r'^tools/post/$',tools.post_url),
    url(r'^data/$',tools.database),
    url(r'^jsontest/$',view.jsontest),
    url(r'^login/',include('django.contrib.auth.urls')),
    url(r'^login/test/$',view.login),
    url(r'^test/index/$',tools.dbtest),
]

