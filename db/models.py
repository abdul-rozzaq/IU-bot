from django.db import models



class Question(models.Model):
    title = models.TextField()
    answer = models.TextField()
    
    
    def __str__(self) -> str:
        return self.title[:50]
    
class User(models.Model):
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    username = models.CharField(max_length=128, null=True)
    telegram_id = models.CharField(max_length=128, null=True)
    
    
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def __str__(self) -> str:
        return self.full_name()