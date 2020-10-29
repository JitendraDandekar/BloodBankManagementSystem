from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    terms_condins = models.CharField(max_length=50, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profilePic/', default='profilePic/profile.jpg', null=True, blank=True)
    per_add = models.CharField(max_length=100, null=True, blank=True)
    temp_add = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Member(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    relation = models.CharField(max_length=20, null=True, blank=True)
    member_gender = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name

class BloodRequest(models.Model):
    BLOOD_TYPE = [('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),
    ('AB-','AB-'),('O+','O+'),('O-','O-'),('Plasma','Plasma'),('Platelet','Platelet')]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    request_for = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    blood_type = models.CharField(max_length=100, choices=BLOOD_TYPE, null=True, blank=True)
    hospital_name = models.CharField(max_length=200, null=True, blank=True)
    hospital_address = models.CharField(max_length=200, null=True, blank=True)
    hospital_contact_no = models.CharField(max_length=200, null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    req_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=100)
    date = models.DateField()
    cert = models.ImageField(upload_to='blood_certificates/')

    def __str__(self):
        return self.user.username