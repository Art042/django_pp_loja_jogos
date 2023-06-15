from django.db import models

class Jogo(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Plataforma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Console(models.Model):
    nome = models.CharField(max_length=100)
    precoporhora = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome

class JogoPlataforma(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    preco_diario = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.jogo.titulo} - {self.plataforma.nome}"


class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    jogo_plataforma = models.ForeignKey(JogoPlataforma, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return f"Locação {self.pk}"


class ItemLocacao(models.Model):
    jogo_plataforma = models.ForeignKey(JogoPlataforma, on_delete=models.CASCADE)
    locacao = models.ForeignKey(Locacao, on_delete=models.CASCADE)
    dias = models.IntegerField()
    quantidade = models.IntegerField()

    def __str__(self):
        return f"Item {self.pk}"


class UtilizacaoConsoleCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

    def __str__(self):
        return f"Utilização {self.pk}"

class Acessorio(models.Model):
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome
