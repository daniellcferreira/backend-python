from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContactForm, NameForm


# Função para criar um novo contato
@permission_required(
    "contacts.add_contact"
)  # Verifica se o usuário tem permissão para adicionar contatos
def create(request):
    if request.method == "POST":  # Verifica se o método é POST
        form = ContactForm(request.POST)  # Preenche o formulário com os dados do POST
        if form.is_valid():  # Valida o formulário
            name = form.cleaned_data["subject"]  # Obtém o nome do campo 'subject'
            form.save()  # Salva o formulário no banco de dados
            return HttpResponseRedirect(
                reverse("contacts:thanks", args=(name,))
            )  # Redireciona para a página de agradecimento
    else:
        form = ContactForm() # Cria um formulário vazio para GET
    return render(request, "contacts/create.html", {"form": form}) # Renderiza o template com o formulário


# Função para obter o nome do usuário
def get_name(request):
    if request.method == "POST": # Verifica se o método é POST
        form = NameForm(request.POST) # Preenche o formulário com os dados do POST
        if form.is_valid(): # Valida o formulário
            name = form.cleaned_data["your_name"] # Obtém o nome do campo 'your_name'
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,))) # Redireciona para a página de agradecimento
    else:
        form = NameForm() # Cria um formulário vazio para GET
    return render(request, "contacts/name.html", {"form": form}) # Renderiza o template com o formulário


# Função de agradecimento
def thanks(request, name): 
    return HttpResponse(f"Obrigado {name}!") # Retorna uma resposta simples de agradecimento
