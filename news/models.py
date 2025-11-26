from django.db import models

class NewsModel(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    rasm = models.ImageField(upload_to='new/images')

    def __str__(self):
        return self.title