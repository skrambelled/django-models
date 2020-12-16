from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f'{self.title} from {self.author}'
