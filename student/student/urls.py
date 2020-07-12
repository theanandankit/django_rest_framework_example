"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from student_api.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/student_list/$', studentlist.as_view(),name='profile_list'),
    url(r'^api/student_grade/$', student_grade_view.as_view(),name='profile_list'),
    url(r'^api/student_details/$', studentdetails.as_view(),name='profile_list'),
    url(r'^api/profile_details/(?P<roll>\d+)/$', student_specific.as_view(),name='profile_list'),
]