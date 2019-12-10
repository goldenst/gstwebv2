# goldenstateweb URL Configuration

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from .views import home_page, about_page, contact_page, login_page, register_page
# from liens.views import (
#     lien_sales_list_view, 
#     lien_sales_detail_view, 
#     lien_sales_featured_detail_view, 
#     lien_sales_featured_view,
#     lien_sales_detail_slug_view
#     )

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register_page),
    path('lien/', include("liens.urls", namespace='liens')),
    # path('featured/', lien_sales_featured_view.as_view()),
    # path('featured/<pk>/', lien_sales_featured_detail_view.as_view()),
    # path('lien/<pk>/', lien_sales_detail_view),
    # path('lien/<slug>/', lien_sales_detail_slug_view.as_view()),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns =  urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns =  urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)