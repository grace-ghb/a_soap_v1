from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

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