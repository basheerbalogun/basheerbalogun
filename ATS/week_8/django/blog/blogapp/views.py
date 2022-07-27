from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import Post

class HomeView(ListView):
    template_name = 'blogapp/home.html'
    queryset = Post.objects.all()
    paginate_by = 2

class PostView(DetailView):
    model = Post
    template_name = 'blogapp/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']

        post = get_object_or_404(Post, pk=pk, slug=slug)
        context['post'] = post
        return context