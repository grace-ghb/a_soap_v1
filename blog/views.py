from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages

from .models import Post


class BlogList(ListView):
    """
    A view that displays the list of published blog posts.
    """
    model = Post
    template_name = "blog/blog.html"
    paginate_by = 4


class BlogDetail(DetailView):
    """
    A view that displays the details of a individual blog post.
    """    
    def get(self, request, pk, *args, **kwargs):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404("Post does not exist")
        
        return render(
            request,
            "blog/blog_detail.html",
            {
                "post": post,
            },
        )


class AddView(CreateView):
    """
    A view to add blog posts.
    """
    def post(self, request, pk, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        blog = get_object_or_404(queryset, pk=pk)
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/add_post.html",
            {
                "post": post,
            },
        )