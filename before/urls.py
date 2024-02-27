from django.contrib import admin
from django.urls import path
from before.views import home,success

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("success",success,name='success'),
]