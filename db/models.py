from django.db import models



class Question(models.Model):
    title = models.TextField()
    answer = models.TextField()
    
    
    def __str__(self) -> str:
        return self.title[:50]