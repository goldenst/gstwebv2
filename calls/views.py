from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View

from django.http import HttpResponseRedirect



from .forms import CallForm
# Create your views here.

def call_receving_view(request):
  call_form = CallForm(request.POST or None)
  context = {
    'title': 'Call Taking',
    'form': call_form,
  }
  return render(request, "calls/rec.html", context)



