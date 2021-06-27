from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Social Sweet Admin"
admin.site.site_title = "Social Sweet Admin"
admin.site.index_title = "Welcome to Social Sweet Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sweet.urls')),
    path('user/', include('user.urls')),
]
