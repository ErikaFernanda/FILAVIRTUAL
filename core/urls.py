from django.urls import path

from . import views

app_name ="filavirtual"
urlpatterns = [
    path("",views.FilaListView.as_view(), name="list"),
    path("<slug:idfila",views.FilaDetailView.as_view(), name="detail"),
]