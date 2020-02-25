from django.db import models

# Create your models here.
from django.db import models
from account.models import Account
# Create your models here.
class Businessowner(models.Model):
    business = models.CharField( max_length=30,blank=True )
    account = models.ForeignKey(
        Account, on_delete = models.CASCADE
    )
    website = models.URLField()
    category =  models.CharField( max_length=20,blank=True )
    legality  = models.FileField()
    

    