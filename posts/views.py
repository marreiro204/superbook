from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from django.http import HttpResponse
from .forms import PostForm

from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, esta é a página inicial de posts!")


def lista_posts(request):
    posts = Post.objects.all().order_by("criado_em")  # busca todos os heróis do banco
    return render(request, "posts/lista_posts.html", {"posts": posts})

def criar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_posts")
    else:
        form = PostForm()
    return render(request, "posts/criar_post.html", {"form": form})

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"

