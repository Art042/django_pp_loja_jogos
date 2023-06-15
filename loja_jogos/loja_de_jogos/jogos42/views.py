from django.shortcuts import render
from .models import Cliente, Jogo, JogoPlataforma, Plataforma
from django.views import View

def cadastrar_cliente(request):
    if request.method == 'POST':
        # Processar o formulário de cadastro de cliente
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        senha = request.POST['senha']

        cliente = Cliente(nome=nome, email=email, telefone=telefone, senha=senha)
        cliente.save()

        return render(request, 'jogos42/cadastro_cliente.html', {'success': True})

    return render(request, 'jogos42/cadastro_cliente.html', {'success': False})


def cadastrar_jogo(request):
    plataformas = Plataforma.objects.all()

    if request.method == 'POST':
        # Processar o formulário de cadastro de jogo
        titulo = request.POST['titulo']
        plataforma_id = request.POST['plataforma']
        preco_diario = request.POST['preco_diario']

        plataforma = Plataforma.objects.get(pk=plataforma_id)
        jogo = Jogo(titulo=titulo)
        jogo.save()

        jogo_plataforma = JogoPlataforma(jogo=jogo, plataforma=plataforma, preco_diario=preco_diario)
        jogo_plataforma.save()

        return render(request, 'jogos42/cadastro_jogo.html', {'success': True, 'plataformas': plataformas})

    return render(request, 'jogos42/cadastro_jogo.html', {'success': False, 'plataformas': plataformas})


def consultar_disponibilidade(request):
    jogos = Jogo.objects.filter(jogoplataforma__locacao__isnull=True)

    return render(request, 'jogos42/consultar_disponibilidade.html', {'jogos': jogos})

class pagina_inicial(View):
    def get(self, request):
        return render(request, 'jogos42/pagina_inicial.html')