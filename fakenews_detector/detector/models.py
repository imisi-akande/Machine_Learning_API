from django.db import models

# Create your models here.


class News(models.Model):
    id = models.IntegerField(primary_key=True)
    headline = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=False)
    fakeness = models.IntegerField()

def __str__(self):
    return self.headline

