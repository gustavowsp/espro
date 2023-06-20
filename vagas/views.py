from django.shortcuts import render
from vagas.models import Vagas


# Create your views here.
def vagas(request):

    vagas = Vagas.objects.all()
    context = {
        'vagas' : {}
    }

    for vaga in vagas:

        context['vagas'][vaga.nome_vaga] = {

            'nome_vaga' : vaga.nome_vaga,
            'foto'      : vaga.foto,
            'salario'   : vaga.salario,
            'local'     : vaga.local,

            }

    return render(
        request,
        'vagas/index.html',
        context
        )