from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GameResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    win = models.BooleanField(default=False)

class GameSettings(models.Model):
    hlOption = models.IntegerField(default=0)
    numPlayersOption = models.IntegerField(default=0)
    dificultyOp = models.IntegerField(default=0)
    jokerOp = models.IntegerField(default=0)

