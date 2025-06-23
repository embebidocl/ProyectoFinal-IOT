from django.contrib import admin
from django.urls import path, include
from clima.views import home_view, home_redirect_view, signup_view, real_time_view

from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('redirect/', home_redirect_view, name='redirect_home'),
    path('tiempo-real/', real_time_view, name='tiempo_real'),
    path('signup/', signup_view, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]

# Servir archivos estáticos en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'clima', 'static'))
