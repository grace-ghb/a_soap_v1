from django.shortcuts import render,get_object_or_404, HttpResponseRedirect, reverse
from django.views import generic, View
from django.views.generic import ListView, DetailView
# from django.core.paginator import Paginator
# from django.contrib import messages
from .models import Post


class BlogList(generic.ListView):
    """
    A view that displays the list of published blog posts.
    """
    model = Post
    template_name = "blog/blog.html"


class BlogDetail(View):
    """
    A view that displays the details of a individual blog post.
    """
    model = Post
    template_name = "blog/blog_detail.html"

    # def get(self, request, slug, *args, **kwargs):
    #     queryset = Post.objects.filter(status=1)
    #     post = get_object_or_404(queryset, slug=slug)
        
    #     return render(
    #         request,
    #         "blog/blog_detail.html",
    #         {
    #             "blog": blog,
    #         },
    #     )
    
    # def post(self, request, slug, *args, **kwargs):
    #     queryset = Post.objects.filter(status=1)
    #     post = get_object_or_404(queryset, slug=slug)        
        
    #     return render(
    #         request,
    #         "blog/blog_detail.html",
    #         {
    #             "blog": blog,                
    #         },
    #     )
