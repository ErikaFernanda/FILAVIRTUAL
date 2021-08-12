from django  import forms




class EmpresaForm(forms.Model):
    nome = forms.CharField(max_length=250)
    

class FuncionarioForm(forms.Model):
    nome = forms.CharField(max_length=250)
    empresa = forms.ForeignKey(Empresa, on_delete=models.CASCADE)
  

class Fila(forms.Model):
    descricao = forms.CharField(max_length=250)
    empresa = forms.ForeignKey(Empresa, on_delete=models.CASCADE)
    funcionario = forms.ForeignKey(Funcionario, on_delete=models.CASCADE)


class FilaPosicao(forms.Model):
    fila = forms.ForeignKey(Fila, on_delete=models.CASCADE)
    user = forms.ForeignKey(User, on_delete=models.CASCADE)
    posicao = forms.IntegerField()


