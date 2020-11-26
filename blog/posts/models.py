from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})
