from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from .forms import PostForm


class IndexView(TemplateView):
    """
    a class based view that renders the index page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Kasra'
        context['posts'] = Post.objects.all()
        return context


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'
    ordering = ['-id']


class PostDetailView(DetailView):
    model = Post


class PostListApiView(TemplateView):
    template_name = "blog/post_list_api.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"


