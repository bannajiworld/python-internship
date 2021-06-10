from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview,name="home"),
    path('about',views.aboutpageview,name="about"),
    path('contact',views.contactpageview,name="contact"),
    path('myform',views.myformpageview,name="myform"),
    path('formprocess',views.process,name="process"),
    path('slist',views.studentlist.as_view(),name="studentlist"),
    

]
