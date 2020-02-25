from django.db import models

class Profile(models.Model):
    # user = models.OneToOneField(User,on_delete = models.CASCADE)
    username = models.CharField( max_length=30,blank=True )
    password = models.CharField( max_length=20,blank=True )
    email = models.CharField( max_length=20,blank=True )
    last_name = models.CharField( max_length=30,blank=True )
    first_name = models.CharField( max_length=30,blank=True )
    GENDER = (('F','Female'), ('M','Male'))
    phoneNo = models.CharField( max_length=13,blank=True )
    sex = models.CharField( max_length=6,blank=True )
    subcity = models.CharField( max_length=20,blank=True )
    woreda = models.IntegerField( blank=True )
    nationality = models.CharField( max_length=30,blank=True ) 
    # birth_date = models.DateField( blank=False )