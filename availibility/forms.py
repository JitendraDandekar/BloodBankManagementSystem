from django import forms
from .models import *

# Create your models here.
class CampForm(forms.ModelForm):
	class Meta:
		model = Camp
		fields = ('title', 'location', 'organizer', 'contact_no', 'date')

class BloodAvailibilityForm(forms.ModelForm):
	class Meta:
		model = BloodAvailibility
		fields = '__all__'

class CampConfirmationForm(forms.ModelForm):
	class Meta:
		model = Camp
		fields = '__all__'

class CareCentreForm(forms.ModelForm):
	class Meta:
		model = CareCentre
		fields = '__all__'