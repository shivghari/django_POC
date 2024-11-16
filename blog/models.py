from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 20)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title
