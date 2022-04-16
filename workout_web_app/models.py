from django.db import models
from django.conf import settings
from django.utils import timezone

class WorkoutMenu(models.Model):
    date_of_activity = models.DateTimeField(default=timezone.now)
    workout_name = models.CharField(max_length=200)
    remarks_column = models.TextField()
    reps = models.IntegerField()
    weight = models.FloatField()
    
    def train(self):
        self.save()
    
    def __str__(self):
        return self.workout_name
    
    
    