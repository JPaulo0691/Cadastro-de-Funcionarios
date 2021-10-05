from os import name
from django.urls import path, include
from .import views 

urlpatterns = [
   
    path('',views.form_funcionarios, name = 'funcionarios_insert'), #inserior dados
    path('<int:id>/',views.form_funcionarios, name = 'funcionarios_update'),# atualização
    path('delete/<int:id>/',views.delete_funcionarios, name = "delete_funcionarios"),
    path('list/', views.lista_funcionarios, name = 'lista_funcionarios'),
    # mostrar todas as gravações de funcionários
]
