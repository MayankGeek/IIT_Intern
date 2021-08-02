from django.db import models

# Create your models here.
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True





class Image(models.Model):
    
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title