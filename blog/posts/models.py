from django.db import models
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'