from django.forms import ModelForm, TextInput, Select

from .models import Alimento, Sabor, Textura, Tecnica, TiposCorte, TipoIngrediente

class AlimentoForm(ModelForm):
    class Meta:
        model = Alimento
        fields = '__all__'
        labels = {
            'tnombre': 'Nombre',
            'csabor': 'Sabor',
            'ctextura': 'Textura'
        }
        widgets = {
            'tnombre': TextInput(attrs={'class': 'form-control'}),
            'csabor': Select(attrs={'class': 'form-control'}),
            'ctextura': Select(attrs={'class': 'form-control'})
        }

class SaborForm(ModelForm):
    class Meta:
        model = Sabor
        fields = '__all__'
        labels = {
            'tnombre': 'Nombre',
        }
        widgets = {
            'tnombre': TextInput(attrs={'class': 'form-control'}),
        }

class TexturaForm(ModelForm):
    class Meta:
        model = Textura
        fields = '__all__'
        labels = {
            'tnombre': 'Nombre',
        }
        widgets = {
            'tnombre': TextInput(attrs={'class': 'form-control'}),
        }

class TecnicaForm(ModelForm):
    class Meta:
        model = Tecnica
        fields = '__all__'
        labels = {
            'tnombre': 'Nombre',
        }
        widgets = {
            'tnombre': TextInput(attrs={'class': 'form-control'}),
        }

class TipoCorteForm(ModelForm):
    class Meta:
        model = TiposCorte
        fields = '__all__'
        labels = {
            'tnombre': 'Nombre',
        }
        widgets = {
            'tnombre': TextInput(attrs={'class': 'form-control'}),
        }

class TipoIngredienteForm(ModelForm):
    class Meta:
        model = TipoIngrediente
        fields = '__all__'
        labels = {
            'tnombre': 'Nombre',
        }
        widgets = {
            'tnombre': TextInput(attrs={'class': 'form-control'}),
        }
