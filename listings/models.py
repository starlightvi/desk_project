from django.db import models
from datetime import date
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):
    list_true="avaiable"
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING) #what to do to listings when realtor gets deleted
    #realtor: INT (FOREIGN KEY [realtor])
    title= models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    description=models.TextField(blank=False)
    price=models.IntegerField()
    ##Amenities 
    parking=models.IntegerField()
    sqft=models.DecimalField(max_digits=5, decimal_places=2)
    Tech_enabled_room=models.BooleanField()
    Private_Cabins=models.BooleanField()
    Open_Workspaces= models.BooleanField()
    Work_Anytime=models.BooleanField()
    Game_Zone=models.BooleanField()
    ##photos 
    photo_main=models.ImageField(upload_to='photo/%Y/%m/%d/') #define where these get uploaded to=> media folder of Django, in date formart
    photo1=models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    photo2=models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    photo3=models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    photo4=models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    photo4=models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    photo4=models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    ##published 
    is_published=models.BooleanField(default=False)
    def __str__(self):
        return self.title
    




