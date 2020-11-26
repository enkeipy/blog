from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text', 'creation_date']
    template_name_suffix = '_update_form'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('all')
