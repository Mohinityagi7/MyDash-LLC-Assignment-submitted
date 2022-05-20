from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=10000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

class Quota(models.Model):
    view = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)