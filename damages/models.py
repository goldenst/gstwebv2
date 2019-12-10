from django.db import models


from drivers.models import Driver
# Create your models here.

class Damage(models.Model):
  driver              = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
  date_of_incident    = models.DateField(blank=True)
  club                = models.CharField(blank=True, max_length=120)
  call_num            = models.IntegerField(blank=True)
  customer_email      = models.CharField(blank=True, max_length=120)
  cust_name           = models.CharField(blank=True, max_length=120)
  cust_phone          = models.CharField(blank=True, max_length=120)
  vehicle             = models.CharField(max_length=120)
  damages             = models.TextField(blank=True, max_length=120)
  status              = models.CharField(blank=True, max_length=120)
  cost_to_gst         = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
  repaired_at         = models.CharField(blank=True, max_length=120)
  closed              = models.BooleanField(default=False)
  closed_date         = models.DateField(auto_now_add=True)
  damages_est         = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
  estimate            = models.FileField(upload_to='damages/', blank=True)
  driver_statement    = models.FileField(upload_to='damages/', blank=True)
  damage_main         = models.ImageField(upload_to='damages/', blank=True)
  damage_2            = models.ImageField(upload_to='damages/', blank=True)
  damage_3            = models.ImageField(upload_to='damages/', blank=True)
  damage_4            = models.ImageField(upload_to='damages/', blank=True)
  damage_5            = models.ImageField(upload_to='damages/', blank=True)
  damage_6            = models.ImageField(upload_to='damages/', blank=True)
  damage_7            = models.ImageField(upload_to='damages/', blank=True)
  damage_8            = models.ImageField(upload_to='damages/', blank=True)
  damage_9            = models.ImageField(upload_to='damages/', blank=True)


  def __str__(self):
    return self.cust_name