from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Member)
admin.site.register(BloodRequest)
admin.site.register(Donation)