from django.urls import path, re_path
from .views import PostList, PostDetailView, PostCreate, PostUpdate, PostDelete

app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(), name='all'),
    path('create/', PostCreate.as_view(), name='create'),
    re_path('(?P<pk>\d+)/update/', PostUpdate.as_view(), name='update'),
    re_path('(?P<pk>\d+)/delete/', PostDelete.as_view(), name='delete'),
    re_path('(?P<pk>\d+)/', PostDetailView.as_view(), name='detail'),
]
