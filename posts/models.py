from django.db import models

# Create your models here.
# This models the characteristic of the data in our database.
class Post(models.Model):
    text=models.TextField()
    
    def __str__(self):
        return self.text[:50]
