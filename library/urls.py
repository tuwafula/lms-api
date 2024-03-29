from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('base/' , include('base.urls')),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

