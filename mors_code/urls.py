from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = i18n_patterns(
    path('super/user/admin/', admin.site.urls),
    path('', include(('apps.mainpage.urls'), namespace='mainpage')),

    path('parameter/', include("apps.parameter.urls")),
    path('ckeditor-secret/', include('ckeditor_uploader.urls')),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
