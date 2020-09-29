from django.db import models
''' model without special offer

class Destination:
    id:int
    name:str
    desc:str
    img:str
    price:str
'''

# Create your models here.
'''
#model with specialoffer
class Destination:
    id:int
    name:str
    desc:str
    img:str
    price:str
    specialoffer:bool
'''
class Destination(models.Model):

    name = models.CharField(max_length=50)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offerpercentage= models.IntegerField()
    specialoffer=models.BooleanField(default='False')
