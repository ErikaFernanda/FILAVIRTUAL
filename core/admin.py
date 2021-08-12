from django.contrib import admin
from .models import Empresa, Fila, FilaPosicao, Funcionario

# Register your models here.
admin.site.register(Fila)
class FilaAdmin(admin.ModelAdmin):
    list_display=("descricao","empresa")

admin.site.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display=("nome")
admin.site.register(FilaPosicao)
class FilaPosicaoAdmin(admin.ModelAdmin):
    list_display=("posicao","usuario")
admin.site.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display=("nome","empresa")
