from django.db import models

class Notice(models.Model):
    title = models.TextField(max_length= 200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    ANSWER_STATUS_CHOICES = [
        ('N', 'Not Answered'),
        ('Y', 'Answered'),
    ]
    question_text = models.CharField(max_length=200)
    password = models.CharField(max_length=8)
    answer_status = models.CharField(max_length=1, choices=ANSWER_STATUS_CHOICES, default='N')

    def __str__(self):
        return self.question_text