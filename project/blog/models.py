from enum import auto
from multiprocessing import AuthenticationError
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  #객체를 처음 생성할때만 업데이트 해준다 date를 
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=100, blank=True)
   

    def __str__(self):
        return self.title #pk값을 리턴하는 것이아니라 타이ㄷ틀값을 리턴하도록
