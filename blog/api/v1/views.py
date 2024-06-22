from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets
from .serializers import PostSerializer, CategorySerializer
from blog.models import Post, Category
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'author')


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


