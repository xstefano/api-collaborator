from django.db import models

# Create your models here.
class Collaborator(models.Model):
    
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    cellphone = models.CharField(max_length=20)
    dateofbirth = models.DateField()
    createdat = models.DateField(auto_now_add=True)
