from django.db import models

# Create your models here.
class MenuItem(models.Model):
    '''model class'''

    name = models.CharField(max_length=255) # one column
    price = models.IntegerField() # data base table

class Reservation(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)