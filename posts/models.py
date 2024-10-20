from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()

    # TO make entry of the DB more descriptive with the first 50 chat of the text entry
    def __str__(self):
        return self.text[:50]
