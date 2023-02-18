
from django.contrib import admin
from django.urls import path, include
from image.api import api

VERSION = 'v1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"api/{VERSION}/", api.urls),
    # path(f"", include('bucket3.urls'))
]
