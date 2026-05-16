"""
URL configuration for LearningManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import views
urlpatterns = [
#path('admin/', admin.site.urls),
path('', views.index, name='index'),
path('index/', views.index, name='index'),
path('logout/', views.index, name='logout'),
path('about/', views.about, name='about'),
path('services/', views.services, name='services'),
path('gallery/', views.gallery, name='gallery'),
path('newstudent/', views.newstudent, name='newstudent'),
path('adminlogin/', views.adminlogin, name='adminlogin'),
path('stafflogin/', views.stafflogin, name='stafflogin'),
path('studentlogin/', views.studentlogin, name='studentlogin'),
path('contact/', views.contact, name='contact'),
path('adminmainpage/', views.adminmainpage, name='adminmainpage'),
path('adminaddstaff/', views.adminaddstaff, name='adminaddstaff'),
path('adminviewstaffs/', views.adminviewstaffs, name='adminviewstaffs'),
path('adminviewstudents/', views.adminviewstudents, name='adminviewstudents'),
path('adminviewreports/', views.adminviewreports, name='adminviewreports'),
path('adminviewcontacts/', views.adminviewcontacts, name='adminviewcontacts'),

path('studentmainpage/', views.studentmainpage, name='studentmainpage'),
path('studentviewprofile/', views.studentviewprofile, name='studentviewprofile'),
path("studentviewchapters1/<str:id>", views.studentviewchapters1, name="studentviewchapters1"),
path('studentviewchapters/', views.studentviewchapters, name='studentviewchapters'),
path('studenttaketest/', views.studenttaketest, name='studenttaketest'),
path('studenttaketest1/', views.studenttaketest1, name='studenttaketest1'),
path('studentviewreports/', views.studentviewreports, name='studentviewreports'),
path('studentviewpythonchapters/', views.studentviewpythonchapters, name='studentviewpythonchapters'),
path('studentviewjavachapters/', views.studentviewjavachapters, name='studentviewjavachapters'),
path('studentviewpython/', views.studentviewpython, name='studentviewpython'),
path('studentviewjava/', views.studentviewjava, name='studentviewjava'),
path('studentviewcertificate/', views.studentviewcertificate, name='studentviewcertificate'),
path("studentviewjavachapters/<str:id>", views.studentviewjavachapters, name="studentviewjavachapters"),
path("studentviewpythonchapters/<str:id>", views.studentviewpythonchapters, name="studentviewpythonchapters"),
]