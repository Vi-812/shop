from django.db import models


class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100) #Привести к списку
    email = models.EmailField(max_length=50)
    password_hash = models.CharField(max_length=20)
    date_registration = models.DateField(auto_now_add=True)
    date_activity = models.DateField()
