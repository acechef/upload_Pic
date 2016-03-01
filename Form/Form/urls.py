"""Form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', 'myform.views.index'),
    url(r'^test$', 'myform.views.test'),
    url(r'^getVCode$', 'myform.views.getVCode'),
    url(r'^verificeVCode$', 'myform.views.verificeVCode'),
    url(r'^saveDream$', 'myform.views.saveDream'),
    url(r'^followdream$', 'myform.views.followdream'),
    url(r'^moredream$', 'myform.views.moredream'),
    url(r'^admin/', include(admin.site.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 在django1.5中，上传图片的设置是这样的：
# --------------------------------------------------------------------------------------------
# 在models.py中，
#      photo=models.ImageField(upload_to=settings.MEDIA_ROOT)
# 在模板中
# 首先{% load staticfiles %}   !注意，不用于1.3的static
# 显示图片：   <img src="{{ obj.photo.url }}"/>   
# django显示图片--->baidu
