from django.contrib import admin
from .models import Cliente, Jogo, Plataforma, JogoPlataforma, Locacao, ItemLocacao, UtilizacaoConsoleCliente, Console, Acessorio
admin.site.register(Cliente)
admin.site.register(Jogo)
admin.site.register(Plataforma)
admin.site.register(JogoPlataforma)
admin.site.register(Locacao)
admin.site.register(ItemLocacao)
admin.site.register(UtilizacaoConsoleCliente)
admin.site.register(Console)
admin.site.register(Acessorio)
