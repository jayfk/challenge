from django.conf import settings
from django.urls import include, path

from jupus.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]

# if we are on the development environment, we want the django devserver to also
# serve the static files. Additionally, we want to have the django debug toolbar
# enabled
if settings.DEBUG:  # pragma: no cover
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    try:
        import debug_toolbar

        urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
    except ImportError:
        pass
