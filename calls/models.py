from django.db.models import Q
from django.conf import settings
from django.db import models
from datetime import datetime
import random
import os

from drivers.models import Driver
from services.models import Service

User = settings.AUTH_USER_MODEL


class Call(models.Model):
  User        = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
  driver      = models.ForeignKey(Driver, null=True, blank=True, on_delete=models.DO_NOTHING)
  services    = models.ManyToManyField(Service, blank=True)
  total       = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
  timestamp   = models.DateTimeField(auto_now_add=True)
  update      = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self)








