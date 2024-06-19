from django.contrib import admin

from blog.models import Post, Category

app_name = 'blog'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'category',
                    'published_date', 'created_date')


# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
