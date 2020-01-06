from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Service

def ServiceListView(request):
  queryset = Service.objects.all()
  context = {
    'object_list' : queryset
  }
  return render(request, 'services/list_view.html', context)


def ServiceDetailView(request):
  queryset = Service.objects.all()
  context = {
    'object_list' : queryset
  }
  return render(request, 'services/detail_view.html', context)


