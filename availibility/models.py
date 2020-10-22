from django.db import models

# Create your models here.
class BloodAvailibility(models.Model):
	location = models.CharField(max_length=50, blank=True, null=True)
	blood_a = models.IntegerField(blank=True, null=True)
	blood_b = models.IntegerField(blank=True, null=True)
	blood_ab = models.IntegerField(blank=True, null=True)
	blood_o = models.IntegerField(blank=True, null=True)
	plasma = models.IntegerField(blank=True, null=True)
	platelet = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.location

class Camp(models.Model):
	title = models.CharField(max_length=50, blank=True, null=True)
	location = models.CharField(max_length=100, blank=True, null=True)
	organizer = models.CharField(max_length=100, blank=True, null=True)
	contact_no = models.IntegerField(blank=True, null=True)
	date = models.DateTimeField(blank=True, null=True)
	confirm = models.BooleanField(default=False, blank=True, null=True)

	def __str__(self):
		return self.organizer

class CareCentre(models.Model):
	clinic_name = models.CharField(max_length=100, blank=True, null=True)
	dr_name = models.CharField(max_length=100, blank=True, null=True)
	address = models.CharField(max_length=200, blank=True, null=True)
	contact = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.clinic_name