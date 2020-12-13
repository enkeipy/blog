from posts.models import Post
from posts.views import PostDetailView

class HomePage(PostDetailView):
    model = Post
    def get_object(self):
        return Post.objects.first()