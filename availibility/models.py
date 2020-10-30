from django.db import models

# Create your models here.
class BloodAvailibility(models.Model):
	location = models.CharField(max_length=50)
	blood_a = models.IntegerField()
	blood_b = models.IntegerField()
	blood_ab = models.IntegerField()
	blood_o = models.IntegerField()
	plasma = models.IntegerField()
	platelet = models.IntegerField()

	def __str__(self):
		return self.location

class Camp(models.Model):
	title = models.CharField(max_length=50)
	location = models.CharField(max_length=100)
	organizer = models.CharField(max_length=100)
	contact_no = models.IntegerField()
	date = models.DateTimeField()
	confirm = models.BooleanField(default=False)

	def __str__(self):
		return self.organizer

class CareCentre(models.Model):
	clinic_name = models.CharField(max_length=100)
	dr_name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	contact = models.IntegerField()

	def __str__(self):
		return self.clinic_name