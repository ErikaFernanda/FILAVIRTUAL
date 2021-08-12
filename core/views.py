from django.views.generic import DetailView, ListView
from .forms import EmpresaForm

from .models import Empresa, Fila

from .models import User

class FilaListView(ListView):
    model = Fila
class FilaDetailView(DetailView):
    model = Fila

class UserListView(ListView):
    model = User
class UserDetailView(DetailView):
    model = User

class EmpresaListView(ListView):
    model = Empresa
class EmpresaDetailView(DetailView):
    model = Empresa

def empresaForm(request):
    form = EmpresaForm()
    return render(request,'empresa_form.html',{'form':form})

