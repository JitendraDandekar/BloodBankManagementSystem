from django.db import models
from django.contrib.auth.models import User

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
        return self.profile.user.get_full_name()