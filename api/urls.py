from django.contrib import admin
from django.urls import path
from . import views
app_name = "api"

urlpatterns = [
    # path('dashboard/',views.dashboard,name = "dashboard"),
    path('addstatic/',views.addStatic,name = "addstatic"),
    path('',views.addStatic,name = "addstatic"),
    path('adddynamic/',views.addDynamic,name = "adddynamic"),
    path('apistatic/',views.apistatic,name = "apistatic"),
    path('apidynamic/',views.apidynamic,name = "apidynamic"),   
]
