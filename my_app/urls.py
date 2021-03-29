from django.urls import path, include
from my_app import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
]
