"""loja_de_jogos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jogos42.views import (
    cadastrar_cliente,
    cadastrar_jogo,
    consultar_disponibilidade,
    pagina_inicial,
)

app_name = 'jogos42'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', pagina_inicial.as_view(), name='pagina_inicial'),
    path('cadastro/cliente/', cadastrar_cliente, name='cadastro_cliente'),
    path('cadastro/jogo/', cadastrar_jogo, name='cadastro_jogo'),
    path('consulta/disponibilidade/', consultar_disponibilidade, name='consultar_disponibilidade'),
]
