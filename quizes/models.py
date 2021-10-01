from django.db import models
import random
# Create your models here.
difficulty_level=(
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard')
)
class QUIZ(models.Model):
    name=models.CharField(max_length=50)
    topic=models.CharField(max_length=50)
    no_of_questions=models.IntegerField()
    time=models.IntegerField(help_text='time to pass quiz')
    required_score=models.IntegerField(help_text='you must get % to pass')
    difficulty=models.CharField(max_length=50,choices=difficulty_level)
    def __str__(self):
        return f'{self.name}-------{self.required_score}'
    def get_questions(self):
        questions=list(self.quiz.all())
        random.shuffle(questions)
        return questions[:self.no_of_questions]
    class Meta:
        verbose_name_plural='quizes'