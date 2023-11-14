from django.db import models

class Notice(models.Model):
    title = models.TextField(max_length= 200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.question_text