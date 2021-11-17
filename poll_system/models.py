from django.db import models
from django.db.models import query_utils


class TopicPoll(models.Model):
    topic = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Topic Poll'
        verbose_name_plural = 'Topic Polls'
        

class Question(models.Model):
    VALUE_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    question = models.CharField(max_length=200)
    poll = models.ForeignKey(TopicPoll, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    anwser = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'

    def __str__(self):
        return self.anwser


class Test(models.Model):
    CHOICE_QUALITY = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    question1 = models.IntegerField(choices=CHOICE_QUALITY, default=0)
    question2 = models.IntegerField(choices=CHOICE_QUALITY, default=0)
    question3 = models.IntegerField(choices=CHOICE_QUALITY, default=0)
    question4 = models.IntegerField(choices=CHOICE_QUALITY, default=0)
    question5 = models.IntegerField(choices=CHOICE_QUALITY, default=0)

    def __str__(self):
       
        return self.question1



    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

        
    
    