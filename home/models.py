from django.db import models

# Create your models here.
class SlideImg(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='slideImages/')

    def __str__(self):
        return self.name