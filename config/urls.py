from django.contrib import admin
from django.urls import path, include # جديد

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), # جديد
]