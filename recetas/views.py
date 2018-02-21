from django.forms import modelform_factory, TextInput, Select
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Alimento, Sabor, Textura, Tecnica, \
                    TiposCorte, TipoIngrediente, CategoriaIngrediente, \
                    IngredienteInfo

# Function For Generic purpose
def entidad(e):
    ents = {
        'alimentos': ['Alimentos', 'Alimento', '', 'lista_alimentos.html'],
        'sabores': ['Sabores', 'Sabor', '', 'lista_generica.html'],
        'texturas': ['Texturas', 'Textura', '', 'lista_generica.html'],
        'tecnicas': ['Técnicas', 'Tecnica', '', 'lista_generica.html'],
        'tipos-corte': ['Tipos de Corte', 'TiposCorte', '', 'lista_generica.html'],
        'tipos-ingrediente': ['Tipos de Ingrediente', 'TipoIngrediente', '', 'lista_generica.html'],
        'categorias-ingrediente': ['Categorías de Ingrediente', 'CategoriaIngrediente', '', 'lista_generica.html'],
        'ingredientes': ['Ingredientes', 'IngredienteInfo', '', 'lista_ingredientes.html']
    }

    return ents.get(e, "null")

def index(request):
    return render(request, 'recetas/index.html')

def elementos(request, url):
    e = entidad(url)
    lista = eval(e[1]).objects.all()

    paginator = Paginator(lista, 10)
    page = request.GET.get('page')

    context = {'entidad': e[0], 'elemento_entidad': url, 'lista': paginator.get_page(page)}
    return render(request, 'recetas/' + e[3], context)

@login_required
def elemento_nuevo(request, url):
    e = entidad(url)

    if request.method == 'POST':
        modelform = modelform_factory(eval(e[1]), fields = '__all__')

        form = modelform(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Elemento registrado.")
            return HttpResponseRedirect("/e/" + url)

    else:
        form = modelform_factory(eval(e[1]),
                                fields = '__all__',
                                labels = {
                                    'tnombre': 'Nombre', 
                                    'csabor': 'Sabor', 
                                    'ctextura': 'Textura',
                                    'calimento': 'Alimento',
                                    'ctecnica': 'Técnica',
                                    'ctipo': 'Tipo',
                                    'ccategoria': 'Categoría',
                                    'ccorte': 'Corte'
                                    },
                                widgets = {
                                    'tnombre': TextInput(attrs={'class': 'form-control'}),
                                    'csabor': Select(attrs={'class': 'form-control'}),
                                    'ctextura': Select(attrs={'class': 'form-control'}),
                                    'calimento': Select(attrs={'class': 'form-control'}),
                                    'ctecnica': Select(attrs={'class': 'form-control'}),
                                    'ctipo': Select(attrs={'class': 'form-control'}),
                                    'ccategoria': Select(attrs={'class': 'form-control'}),
                                    'ccorte': Select(attrs={'class': 'form-control'}),
                                    })(label_suffix="")
            
    return render(request, 'recetas/form_generico.html', {'form': form})

@login_required
def elemento_edit(request, url, cid):
    e = entidad(url)

    if request.method == 'POST':
        instance = get_object_or_404(eval(e[1]), cid = cid)
        modelform = modelform_factory(eval(e[1]), fields = '__all__')
        form = modelform(request.POST or None, instance = instance)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Elemento actualizado.")
            return HttpResponseRedirect("/e/" + url)

    else:
        instance = get_object_or_404(eval(e[1]), cid = cid)
        modelform = modelform_factory(eval(e[1]), 
                                    fields = '__all__',
                                    labels = {
                                    'tnombre': 'Nombre', 
                                    'csabor': 'Sabor', 
                                    'ctextura': 'Textura',
                                    'calimento': 'Alimento',
                                    'ctecnica': 'Técnica',
                                    'ctipo': 'Tipo',
                                    'ccategoria': 'Categoría',
                                    'ccorte': 'Corte'
                                    },
                                widgets = {
                                    'tnombre': TextInput(attrs={'class': 'form-control'}),
                                    'csabor': Select(attrs={'class': 'form-control'}),
                                    'ctextura': Select(attrs={'class': 'form-control'}),
                                    'calimento': Select(attrs={'class': 'form-control'}),
                                    'ctecnica': Select(attrs={'class': 'form-control'}),
                                    'ctipo': Select(attrs={'class': 'form-control'}),
                                    'ccategoria': Select(attrs={'class': 'form-control'}),
                                    'ccorte': Select(attrs={'class': 'form-control'}),
                                    })

        form = modelform(request.POST or None, instance = instance, label_suffix = "")

    return render(request, 'recetas/form_generico.html', {'form': form})

@login_required
def elemento_del(request, url, cid):
    e = entidad(url)
    elemento = get_object_or_404(eval(e[1]), cid = cid)
    elemento.delete()
    messages.add_message(request, messages.SUCCESS, "Elemento eliminado.")
    return HttpResponseRedirect("/e/" + url)
