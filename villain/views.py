from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  Villains
from .forms import VillainForm

def hello_villains(request):
    return HttpResponse("Bem-vindo ao módulo Vilões!")

def lista_viloes(request):
    viloes = Villains.objects.all()  # busca todos os vilões do banco
    return render(request, "villain/lista.html", {"viloes": viloes})



def criar_vilao(request):
    if request.method == "POST":
        form = VillainForm(request.POST, request.FILES)  # <--- importante request.FILES
        if form.is_valid():
            form.save()
            return redirect('lista_villains')
    else:
        form = VillainForm()

    return render(request, "villain/form_villain.html", {"form": form})



