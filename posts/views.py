from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
from comments.models import Comentario
from comments.forms import ComentarioForm

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

def detalhe_post(request, pk):
    post = Post.objects.get(pk=pk)
    comentarios = post.comentarios.all().order_by("-criado_em")

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()  
            return redirect("post_detail", pk=post.pk)
    else:
        form = ComentarioForm()

    return render(request, "posts/post_detail.html", {
        "post": post,
        "comentarios": comentarios,
        "form": form
    })

class PostListView(ListView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "posts"

