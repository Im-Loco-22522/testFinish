from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=100)
    pass_count = models.PositiveIntegerField(default=0)
    pass_percentage = models.PositiveIntegerField(default=50)

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    difficulty = models.PositiveIntegerField(default=1)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
