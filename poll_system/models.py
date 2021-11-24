from django.db import models



class Test(models.Model):
    CHOICE_QUALITY = [
        (1, 1),
        (2, 2),
        (3, 3),
    ]
    question1 = models.IntegerField(choices=CHOICE_QUALITY)
    question2 = models.IntegerField(choices=CHOICE_QUALITY)
    question3 = models.IntegerField(choices=CHOICE_QUALITY)
    question4 = models.IntegerField(choices=CHOICE_QUALITY)
    question5 = models.IntegerField(choices=CHOICE_QUALITY)
    question6 = models.IntegerField(choices=CHOICE_QUALITY)
    question7 = models.IntegerField(choices=CHOICE_QUALITY)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    option1 = models.CharField(max_length=100 
    , blank=True, null=True)
    option2 = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        test_id = str(self.id)
       
        return test_id



    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

        
    
    