from django.db import models
class Velog(models.Model):
    title = models.CharField(max_length=70)
    
    def __str__(self):
        return self.title
# Create your models here.
