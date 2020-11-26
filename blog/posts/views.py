from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class PostList(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'text']


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name_suffix = '_update_form'


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('all')
