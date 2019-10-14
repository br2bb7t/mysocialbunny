"""mysocialbunny URLs module."""

# Django
from django.contrib import admin
from mysocialbunny.settings import base as settings
# from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:    
    import debug_toolbar

    urlpatterns = urlpatterns + [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     