from django.urls import path

from .views import (
    call_receving_view,
    )

app_name = 'calls'

urlpatterns = [
    path('', call_receving_view, name='calls'),
    # path('<pk>/', damage_detail_view, name='detail'),
]