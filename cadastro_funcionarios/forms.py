from django import forms
from .models import Funcionarios


class FormFuncionarios(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = ('nomeCompleto', 'matricula', 'fone', 'posicao')
        labels = {
            'nomeCompleto': 'Nome Completo',
            'matricula': 'Matrícula',     
            'posicao': 'Cargo'
        }
    
    def __init__(self, *args, **kwargs):
        super(FormFuncionarios, self).__init__(*args, **kwargs)
        self.fields['posicao'].empty_label = "Escolha o cargo"
        self.fields['matricula'].required = False