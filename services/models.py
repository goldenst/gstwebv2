from django.db import models

# Create your models here.
class Service(models.Model):
  title           = models.CharField(max_length=120)
  description     = models.TextField()
  price           = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)


  def __str__(self):
    return self.title
