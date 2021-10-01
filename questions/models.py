from quizes.models import QUIZ
from django.db import models
from quizes.models import *
# Create your models here.
class QUESTION(models.Model):
    text=models.CharField(max_length=200)
    quiz=models.ForeignKey(QUIZ,related_name='quiz' , on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
    def get_answers(self):
        return self.answer.all()
class ANSWER(models.Model):
    text=models.CharField(max_length=50)
    question=models.ForeignKey(QUESTION, related_name='answer', on_delete=models.CASCADE)
    solve=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.question.text}---{self.text}---{self.solve}'