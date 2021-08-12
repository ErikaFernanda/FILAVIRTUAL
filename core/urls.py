from django.urls import path

from . import views

app_name ="filavirtual"
urlpatterns = [
    path("/filas/",views.FilaListView.as_view(), name="list"),
    path("/fila/<int:pk>",views.FilaDetailView.as_view(), name="detail"),
    path("/empresas/",views.EmpresaListView.as_view(), name="list"),
    path("/empresa/<int:pk>",views.EmpresaDetailView.as_view(), name="detail"),
    
]