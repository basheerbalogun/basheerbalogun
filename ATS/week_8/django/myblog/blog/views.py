
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, DeleteView, CreateView, UpdateView

from .models import Author, Post, Profile, CommentPost
from .forms import CommentForm


def index(request):
    return render(request, 'blog/base.html')


class BlogListView(ListView):
    model = Post
    ordering = ['date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Post.active_object.all()


class PostDetailView(FormMixin,DetailView):
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['active_comment'] = CommentPost.active_object.all()
        return context


# class AuthorDetailView(DetailView):
#     model = Post
#     template_name = 'blog/author_detail.html'
#     ordering = ['-date_posted']
#
#     def get_context_data(self, **kwargs):
#         context = super(AuthorDetailView, self).get_context_data(**kwargs)
#         context['author'] = get_object_or_404(Post, id=self.kwargs['pk'])
#         return context

def author_detail(request, pk):
    author = get_object_or_404(Author, id=pk)
    author_articles = author.post_set.all()
    author_post_number = author_articles.count()
    post = Post.objects.all()
    context ={
        "author_articles":author_articles,
        'author': author,
        'post': post,
        'author_post_number': author_post_number,
    }
    return render(request, 'blog/author_detail.html', context)


class AuthorListView(ListView):
    model = Post
    template_name = 'blog/author_list.html'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'blog/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['profile-detail'] = get_object_or_404(Profile, id=self.kwargs['pk'])
        return context


@login_required()
def comment(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(id=pk)
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse("post-detail", args=[pk]))
    context = {
        'form': form
    }

    return render(request, 'blog/post_detail.html', context)


class CommentPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CommentPost
    success_url = '/'
    template_name = 'blog/commentpost_delete_confirm.html'

    def test_func(self):
        commentpost = self.get_object()
        if self.request.user == commentpost.user:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/new_post.html'

    # def form_valid(self, form):
    #     author = Author.objects.filter(id=self.request.user.id).first()
    #     form.instance.author = author
    #     return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']


def hide_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.is_hidden = not post.is_hidden
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def hide_comment(request, pk):
    comment = get_object_or_404(CommentPost, id=pk)
    comment.is_hidden = not comment.is_hidden
    comment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

