from django import forms
from django.contrib.auth.models import User
from .models import *

# Create your forms here.
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'profile_pic', 'per_add', 'temp_add', 'dob')
        widgets = {
        	'dob' : forms.DateInput(attrs={'type':'date'}),
        }

GENDER = (('', 'Select'), ('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'))
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('full_name', 'relation', 'member_gender', 'age', 'birthdate')
        widgets = {
        	'member_gender' : forms.Select(choices=GENDER),
        	'birthdate' : forms.DateInput(attrs={'type': 'date'}),
        }