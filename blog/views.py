from django.shortcuts import render,get_object_or_404, HttpResponseRedirect, reverse
from .models import Post
from django.views import generic, View
from django.core.paginator import Paginator
from django.contrib import messages


class BlogList(generic.ListView):
    """
    A view that displays the list of published blog posts.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html"
    paginate_by = 3


class BlogDetail(View):
    """
    A view that displays the details of a individual blog post.
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        
        return render(
            request,
            "blog/blog_detail.html",
            {
                "blog": blog,
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)        
        
        return render(
            request,
            "blog/blog_detail.html",
            {
                "blog": blog,                
            },
        )
