from rest_framework import serializers
from accounts.models import Profile
from blog.models import Post, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'image', 'content', 'snippet', 'relative_url', 'absolute_url',
                  'created_date', 'published_date', 'status', 'author']
        read_only_fields = ['author']

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)

        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('absolute_url')
            rep.pop('relative_url')
            rep.pop('snippet')
        else:
            rep.pop('content')

        rep['category'] = CategorySerializer(instance.category, context={'request': request}).data
        return rep

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id=self.context['request'].user.id)
        return super().create(validated_data)




