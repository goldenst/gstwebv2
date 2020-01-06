# goldenstateweb URL Configuration
from django.urls import path

from .views import (
    ServiceListView,
    ServiceDetailView,
    )

app_name = 'services'

urlpatterns = [
   
    path('', ServiceListView, name='list'),
    # path('featured/', lien_sales_featured_view.as_view()),
    # path('featured/<pk>/', lien_sales_feature'd_detail_view.as_view()),
    path('<pk>/', ServiceDetailView, name='detail'),
]