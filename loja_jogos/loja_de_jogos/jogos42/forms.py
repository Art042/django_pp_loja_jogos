from django import forms
from .models import Cliente, Jogo, JogoPlataforma

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'senha']

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['titulo']

class JogoPlataformaForm(forms.ModelForm):
    class Meta:
        model = JogoPlataforma
        fields = ['jogo', 'plataforma', 'preco_diario']
