from django.db import models
from django.contrib.auth.models import User

import pandas as pd
  
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from . import services
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation




codes = services.get_country_codes()
countries = []
for code in codes:
    newTuple = tuple([code["code"],code["name"]])
    countries.append(newTuple)


# Create your models here.


class Post(models.Model):
    countries = countries

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=3, choices=countries, default = 'HRV')

    class Meta:
        ordering = ['-dateCreated']
   
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Posted by {}: {}'.format(self.user, self.content)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    dateCreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-dateCreated']
   

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Commented by {}: {}'.format(self.user, self.content)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})

 



