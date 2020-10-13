from django import forms
from .models import *

# Create your models here.
class CampForm(forms.ModelForm):
	class Meta:
		model = Camp
		fields = ('title', 'location', 'organizer', 'contact_no', 'date')
