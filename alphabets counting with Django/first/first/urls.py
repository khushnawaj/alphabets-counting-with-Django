from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('contact/',views.contact),
    path('resume/',views.resume),
    path('stringinput/',views.stringinput),
]
