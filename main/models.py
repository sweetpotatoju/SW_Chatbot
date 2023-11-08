from django.db import models

class Notice(models.Model):
    title = models.TextField(max_length= 200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
