from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=120, null=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.author