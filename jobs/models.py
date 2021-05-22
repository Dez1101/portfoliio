from django.db import models

# Create your models here.

# models.Model allows us us to create this new class in python called Jobs snd gives us permission to save 
# this object or to be clear the attributes of these objects into the database

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    #the 2 variables above image and summary are the attributes/properties to be save to the database
    #to know where to get the fields for the models google search django models field