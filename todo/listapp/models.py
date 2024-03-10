from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):

    detail=models.CharField(max_length=500)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    iscompleted=models.IntegerField(default=0)

    def __str__(self):
        return self.detail