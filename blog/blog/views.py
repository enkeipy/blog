from django.views.generic import DetailView
from posts.models import Post
from django.shortcuts import get_object_or_404

class HomePage(DetailView):
    model = Post
    def get_object(self):
        return Post.objects.last()