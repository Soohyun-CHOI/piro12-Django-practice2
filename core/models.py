from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)  # 글자수 제한
    content = models.TextField()
    author = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)  # 만든 즉시 시간 입력
    updated_at = models.DateTimeField(auto_now=True)  # 업데이트 될 때마다 시간 입력
