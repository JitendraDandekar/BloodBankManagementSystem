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

CHOICE = (('True','Yes'),('False','No'))
class AdminPanelUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'is_staff')
        widgets = {
            'is_staff' : forms.Select(choices=CHOICE, attrs={'style':'width:50%'})
        }

class AdminPanelProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'per_add' : forms.TextInput(attrs={'style':'width: 90%;'}),
            'temp_add' : forms.TextInput(attrs={'style':'width: 90%;'}),
            'dob' : forms.DateInput(attrs={'type':'date'}),
            'gender' : forms.Select(choices=GENDER),
        }

class AdminPanelMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {
            'birthdate' : forms.DateInput(attrs={'type':'date'}),
            'member_gender' : forms.Select(choices=GENDER)
        }