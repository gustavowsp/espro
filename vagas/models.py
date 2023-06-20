from django.db import models

# Create your models here.
class Vagas(models.Model):

    nome_vaga = models.CharField(max_length=20)
    foto = models.ImageField(upload_to=f'images/%Y/%m/%d')
    salario = models.IntegerField()
    local = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.nome_vaga