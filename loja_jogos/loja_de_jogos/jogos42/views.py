from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def index(request):
    return render(request, 'jogos42/index.html')

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  # Redireciona para a página de listagem de clientes
    else:
        form = ClienteForm()
    
    return render(request, 'jogos42/formulario.html', {'form': form})
