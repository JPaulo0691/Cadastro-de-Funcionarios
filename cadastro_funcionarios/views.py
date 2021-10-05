from manage import main
from django.shortcuts import redirect, render
from .forms import FormFuncionarios
from .models import Funcionarios

# Create your views here.


def lista_funcionarios(request):
    context = {'lista_funcionarios':Funcionarios.objects.all()}
    return render(request, "cadastro_funcionarios/lista_funcionarios.html",context)

def form_funcionarios(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = FormFuncionarios()
        else:
            funcionarios = Funcionarios.objects.get(pk = id)
            form = FormFuncionarios(instance = funcionarios)
        return render(request, "cadastro_funcionarios/form_funcionarios.html",{'form': form})
    else:
        if id == 0:
            form = FormFuncionarios(request.POST)
        else:
            funcionarios = Funcionarios.objects.get(pk = id)
            form = FormFuncionarios(request.POST, instance = funcionarios)
        if form.is_valid():
            form.save()
        return redirect('/funcionarios/list')

def delete_funcionarios(request,id):
    funcionarios = Funcionarios.objects.get(pk = id)
    funcionarios.delete()
    return redirect('/funcionarios/list')