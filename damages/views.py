from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Damage

# ----------------- list view ------------------------

def damage_list_view(request):
  queryset = Damage.objects.all()
  context = {
    'title': ' Damages',
    'object_list': queryset
  }
  return render(request, "damages/list.html", context)


# ----------------  detail View ---------------------------

def damage_detail_view(request, pk=None, *args, **kwargs):
  instance = Damage.objects.get_by_id(pk)
  if instance is None:
    raise Http404("Damage does not Exsist!")
  context = {
    'title': 'Damage Details',
    'object': instance
  }
  return render(request, "damages/detail.html", context)