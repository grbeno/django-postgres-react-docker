from django.contrib import admin
from django.urls import path, re_path, include
from helloworld.views import React


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('helloworld.urls')),

    # React
    re_path(r'^.*$', React.as_view(), name='frontend'),
]
