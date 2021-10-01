from django.db import models
from quizes.models import *
from django.contrib.auth.models import User
# Create your models here.
class RESULT(models.Model):
    quiz=models.ForeignKey(QUIZ,related_name='quize',on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    result=models.FloatField()
    def __str__(self):
        return str(self.id)