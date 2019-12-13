# goldenstateweb URL Configuration

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from .views import home_page, about_page, contact_page, login_page, register_page


urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register_page),
    path('lien/', include("liens.urls", namespace='liens')),
    path('garage/', include("garage.urls", namespace='garage')),
    path('damages/', include("damages.urls", namespace='damages')),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns =  urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns =  urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)