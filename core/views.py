from django.views.generic import DetailView, ListView

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

