from django.db import models

# Create your models here.
from django.db import models

# 공지 추가 TABLE
class Notice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# 질문 답변 TABLE
class QATable(models.Model):
    question_content = models.TextField()
    question_summary = models.CharField(max_length=255)
    answer_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_summary