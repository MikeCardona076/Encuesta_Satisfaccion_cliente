from django.db import models


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
