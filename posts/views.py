from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from django.http import HttpResponse

from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, esta é a página inicial de posts!")


def lista_posts(request):
    posts = Post.objects.all()  # busca todos os heróis do banco
    return render(request, "posts/lista_posts.html", {"posts": posts})


class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"

