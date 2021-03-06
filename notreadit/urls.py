from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('readit.urls'), name='readit-urls'),
    path('accounts/', include('allauth.urls')),
]
