from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('bikeoffers.urls')),
    path('admin/', admin.site.urls),
]
