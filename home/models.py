from django.db import models
class Velog(models.Model):
    title = models.CharField(max_length=70)
    author = models.TextField(default='')
    date = models.TextField(default='')
    
    def __str__(self):
        return f'Velog({self.title}, {self.author}, {self.date})'