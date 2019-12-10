from django.db import models

# Create your models here.
class Driver(models.Model):
  name      = models.CharField(max_length=200)
  phone     = models.CharField(max_length=20)
  email     = models.CharField(max_length=50)
  hireDate  = models.DateField(blank=True)
  
  def __str__(self):
    return self.name