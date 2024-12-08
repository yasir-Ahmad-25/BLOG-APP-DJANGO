from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='placeholder.jpg' , blank=True)

    def __str__(self):
        return self.title
    