from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()


# -------------  Call form --------------------

class CallForm(forms.Form):


  call_date             = forms.DateField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder": "Date"}))
  driver                = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder": "Driver"}))
  truck                 = forms.DateField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder": "Truck"}))

# -------- cust info --------

  customer                = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder": "Customer"}))
  customer_address        = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder": "Address"}))
  customer_phone          = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder": "Phone"}))
  customer_email          = forms.CharField(widget=forms.EmailInput(attrs={"class" : "col-lg-4 form-control", "placeholder": "Email"})) 

# -------------

  location                = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder": "Location"}))
   
  destination             = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder": "Destination"}))

#  ------------------ Vehicle info
 
  year             = forms.IntegerField(widget=forms.TextInput(attrs={"class" : "col-lg-1 form-control", "placeholder": "Year"}))
  
  make             = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder": "Make"}))

  model             = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder": "Model"}))

  vin             = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder": "Vin #"}))

  plate         = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder" : "Licence Plate"}))

  state        = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder" : "State"}))

  color         = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder" : "Color"}))
  
  # ------------------------- services / charges -------------------------------------

  services         = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder" : "Services"}))

  ammount         = forms.CharField(widget=forms.TextInput(attrs={"class" : "col-lg-4 form-control", "placeholder" : "Ammount"}))