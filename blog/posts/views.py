from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from hitcount.views import HitCountDetailView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(ListView):
    model = Post
    paginate_by = 3


class PostDetailView(HitCountDetailView):
    model = Post
    count_hit = True

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text', 'image']


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text', 'creation_date', 'image']
    template_name_suffix = '_update_form'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:all')
