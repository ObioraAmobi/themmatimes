"""the_mma_times URL Configuration

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
from mmatimes_app import views as mmatimes_views
from contact_app import views as contact_views
from .settings import MEDIA_ROOT
from django.views.static import serve
from accounts_app import views as accounts_views
from django.contrib.staticfiles import views as static_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mmatimes_views.post_list, name='index'),
    url(r'^(?P<id>\d+)/$', mmatimes_views.post_detail, name='post_detail'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^//logout/$', accounts_views.logout, name='logout'),

    # Media root for images
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    #Static files for Heroku
    url(r'^static/(?P<path>.*)$', static_views.serve),
]