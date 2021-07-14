from django.db import models
from django.db.models.expressions import F
from django.db.models.signals import pre_save

CHOICES = (
    ("male", "male"),
    ("female", "female"),

)
class State(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.OneToOneField(State,on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(City, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    literate = models.BooleanField(default=False)
    
    graduate = models.BooleanField(default=False)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    gender = models.CharField(
        max_length = 20,
        choices = CHOICES,
        default = '1'
        )
    def __str__(self):
        return self.name
    
