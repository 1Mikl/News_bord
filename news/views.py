from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = "dataCreate"
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class PostDetal(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'