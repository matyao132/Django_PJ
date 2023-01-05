from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post

class Index(ListView):
    template_name = "macyao_blog/top.html"
    model = Post
    context_object_name = 'posts'