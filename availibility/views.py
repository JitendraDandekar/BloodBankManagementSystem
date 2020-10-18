from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def availibility(request):
	availibility = BloodAvailibility.objects.all()
	return render(request, 'availibility.html', {'availibility': availibility})

def camp(request):
	camp_form = CampForm()
	if request.method == 'POST':
		camp_form = CampForm(request.POST)
		if camp_form.is_valid():
			camp_form.save()
			messages.info(request, 'Thank You For Scheduling Us.. We Will Call You !')
			return redirect('camp')
	else:
		camps = Camp.objects.all()
		return render(request, 'camp.html', {'camps': camps, 'campform':camp_form})

def care_centres(request):
	carecentres = CareCentre.objects.all()
	return render(request, 'carecentres.html', {'carecentres':carecentres})