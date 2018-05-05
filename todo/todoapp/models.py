from django.db import models

# Create your models here.
class ToDo(models.Model):
    id = models.IntegerField(primary_key=True,default=1);
    name = models.CharField(max_length=200);
    createdAt = models.DateTimeField('createdAt');