from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('persius/', include('main.urls')),
    path('admin/', admin.site.urls),
]
