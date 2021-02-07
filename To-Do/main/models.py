from django.db import models

# Create your models here.

# 질문 & 답변 모델
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_data = models.DateTimeField()

class Answer(models.Model):
    # EP] ForignKey = 질문 모델 속성 가져오기, on_delete = models.CASCADE = 질문 모델 속성이 삭제되면 답변 속성도 삭제하기. 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_data = models.DateTimeField()