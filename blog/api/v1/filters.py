from django_filters import rest_framework as filters
from blog.models import Post


class PostFilters(filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            "category": ["exact", "in"],
            "author": ["exact"],
            "status": ["exact"],
        }