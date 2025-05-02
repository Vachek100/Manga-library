from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # For built-in auth (login/logout)
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', include('library.auth_urls')),  # Separate auth URLs
    path('', include('library.urls')),  # Your manga URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
