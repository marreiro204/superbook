
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hero
from django.views.generic import ListView
from .forms import ContatoForm
from .forms import HeroForm

def hello_heroes(request):
    return HttpResponse("Bem-vindo ao módulo Heroes!")

def lista_herois(request):
    herois = Hero.objects.all()  # busca todos os heróis do banco
    return render(request, "heroes/lista.html", {"herois": herois})

class HeroListView(ListView):
    model = Hero
    template_name = "heroes/lista.html"
    context_object_name = "herois"

def contato_view(request):
    form = ContatoForm()  # formulário vazio

    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Aqui você poderia enviar um e-mail ou salvar no banco
            print(form.cleaned_data)
            return render(request, "heroes/contato_sucesso.html")

    return render(request, "heroes/contato.html", {"form": form})

def criar_heroi(request):
    if request.method == "POST":
        form = HeroForm(request.POST, request.FILES)  # <--- importante request.FILES
        if form.is_valid():
            form.save()
            return redirect('lista_herois')
    else:
        form = HeroForm()

    return render(request, "heroes/form_heroi.html", {"form": form})


