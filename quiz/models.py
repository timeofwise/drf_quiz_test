from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()

#모델 작성이 끝나면 시리얼라이저를 만들어야 함
#시리얼라이저는 장고 모델 데이터를 JSON타입으로 바꿔주는(직렬화) 코드임