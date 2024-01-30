from django.db import models

# Create your models here.
class Musician(models.Model):
    firstName= models.CharField(max_length= 50)
    lastName= models.CharField(max_length= 50)
    email= models.CharField(max_length= 200)
    phoenNo= models.CharField(max_length= 11)
    instrument_type= models.CharField(max_length= 50)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'