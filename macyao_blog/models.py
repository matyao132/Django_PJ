from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title