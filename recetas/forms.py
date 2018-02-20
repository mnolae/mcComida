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
