from django.db import models

class Burgers(models.Model): #하나의 테이블 생성 
    name = models.CharField(max_length = 20)
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name 