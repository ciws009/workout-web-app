from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class WorkoutMenu(models.Model):
    workout_name = models.CharField(max_length=200)
    remarks_column = models.TextField()
    reps = models.IntegerField()
    weight = models.FloatField()
    
    def train(self):
        self.save()
    
    def __str__(self):
        return self.workout_name
    
    
    