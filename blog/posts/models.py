from django.db import models
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})
