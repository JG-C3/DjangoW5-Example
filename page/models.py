from django.db import models

# Create your models here.
# [코드 작성] Post 모델 작성
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)