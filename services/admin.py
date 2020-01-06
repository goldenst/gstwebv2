from django.contrib import admin

# Register your models here.
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
  list_display = ('id','title', 'price')


admin.site.register(Service, ServiceAdmin)