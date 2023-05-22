from django.db import models

# Create your models here.


class Note(models.Model): #inherit from models
    body = models.TextField(null=True, blank=True) #we can submit a form with no values
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) #only take a time stamp on the creation of model 

    def __str__(self):
        return self.body[0:50]