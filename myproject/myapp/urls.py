from django.conf import settings # new
from django.conf.urls.static import static # new
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import *;
urlpatterns=[
    path("",home,name='home'),
    path("login/",login,name='login'),
    path("signup/",signup,name='signup'),
    path("addBook/<int:user_id>",addBook,name='addbook')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()