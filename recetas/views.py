from django.forms import modelform_factory, TextInput, Select, CheckboxInput, Textarea
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Alimento, Sabor, Textura, Tecnica, \
                    TiposCorte, TipoIngrediente, CategoriaIngrediente, \
                    IngredienteInfo, RecetasParciales, RecetasCompuestas

# Function For Generic purpose
# [Nombre entidad, entidad, template, menú level, modal size]
def entidad(e):
    ents = {
        'alimentos': ['Alimentos', 'Alimento', 'lista_alimentos.html', 0, False],
        'sabores': ['Sabores', 'Sabor', 'lista_generica.html', 0, False],
        'texturas': ['Texturas', 'Textura', 'lista_generica.html', 0, False],
        'tecnicas': ['Técnicas', 'Tecnica', 'lista_generica.html', 0, False],
        'tipos-corte': ['Tipos de Corte', 'TiposCorte', 'lista_generica.html', 0, False],
        'tipos-ingrediente': ['Tipos de Ingrediente', 'TipoIngrediente', 'lista_generica.html', 0, False],
        'categorias-ingrediente': ['Categorías de Ingrediente', 'CategoriaIngrediente', 'lista_generica.html', 0, False],
        'ingredientes': ['Ingredientes', 'IngredienteInfo', 'lista_ingredientes.html', 1, False],
        'recetas-simples': ['Recetas Simples', 'RecetasParciales', 'lista_generica.html', 2, True],
        'recetas-compuestas': ['Recetas Compuestas', 'RecetasCompuestas', 'lista_generica.html', 2, True]
    }

    return ents.get(e, "null")

def index(request):
    return render(request, 'recetas/index.html')

def elementos(request, url):
    e = entidad(url)
    lista = eval(e[1]).objects.all()

    paginator = Paginator(lista, 10)
    page = request.GET.get('page')

    context = {'entidad': e[0], 'elemento_entidad': url, 'lista': paginator.get_page(page), 'lvl': e[3], 'modal_lg': e[4]}
    return render(request, 'recetas/' + e[2], context)

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
                                    'ccorte': 'Corte',
                                    'lacomp': 'Acompañamiento',
                                    'tdetalle': 'Detalle',
                                    },
                                widgets = {
                                    'tnombre': TextInput(attrs={'class': 'form-control boxed'}),
                                    'csabor': Select(attrs={'class': 'form-control boxed'}),
                                    'ctextura': Select(attrs={'class': 'form-control boxed'}),
                                    'calimento': Select(attrs={'class': 'form-control boxed'}),
                                    'ctecnica': Select(attrs={'class': 'form-control boxed'}),
                                    'ctipo': Select(attrs={'class': 'form-control boxed'}),
                                    'ccategoria': Select(attrs={'class': 'form-control'}),
                                    'ccorte': Select(attrs={'class': 'form-control boxed'}),
                                    'lacomp': CheckboxInput(attrs={'class': 'checkbox'}),
                                    'tdetalle': Textarea(attrs={'class': 'form-control boxed'}),
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
                                    'ccorte': 'Corte',
                                    'lacomp': 'Acompañamiento',
                                    'tdetalle': 'Detalle',
                                    },
                                widgets = {
                                    'tnombre': TextInput(attrs={'class': 'form-control boxed'}),
                                    'csabor': Select(attrs={'class': 'form-control boxed'}),
                                    'ctextura': Select(attrs={'class': 'form-control boxed'}),
                                    'calimento': Select(attrs={'class': 'form-control boxed'}),
                                    'ctecnica': Select(attrs={'class': 'form-control boxed'}),
                                    'ctipo': Select(attrs={'class': 'form-control boxed'}),
                                    'ccategoria': Select(attrs={'class': 'form-control boxed'}),
                                    'ccorte': Select(attrs={'class': 'form-control boxed'}),
                                    'lacomp': CheckboxInput(attrs={'class': 'checkbox'}),
                                    'tdetalle': Textarea(attrs={'class': 'form-control boxed'}),
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
