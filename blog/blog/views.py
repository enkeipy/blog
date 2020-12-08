from django.views.generic import TemplateView
from django.views.generic import ListView
from posts.views import PostList
from posts.models import Post

class HomePage(ListView):
    model = Post
    paginate_by = 6
    template_name = 'index.html'