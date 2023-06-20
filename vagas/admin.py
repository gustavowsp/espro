from django.contrib import admin
from vagas.models import Vagas

# Register your models here.
@admin.register(Vagas)
class VagasAdmin(admin.ModelAdmin):
    list_display = ['nome_vaga','salario']
    search_fields = ['nome_vaga','salario']