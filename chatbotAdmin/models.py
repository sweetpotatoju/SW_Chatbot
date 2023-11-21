
# Create your models here.
from django.db import models
from main.models import Question

# 공지 추가 TABLE
class Notice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# 질문 답변 TABLE
class QATable(models.Model):
    # main Question model 외래키 참조
    q = models.ForeignKey('main.Question', on_delete=models.CASCADE)

    #question_summary = models.CharField(max_length=255)
    a = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    label = models.IntegerField(default=0)

    def __str__(self):
        return self.a



