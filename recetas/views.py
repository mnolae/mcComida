from django.forms import modelform_factory
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Ingrediente, Sabor, Textura, Tecnica, TiposCorte, TipoIngrediente, CategoriaIngrediente
from .forms import IngredienteForm, SaborForm, TexturaForm, TecnicaForm, TipoCorteForm, TipoIngredienteForm

## Funciones genéricas

def entidad(e):
    ents = {
        'ingredientes': ['Ingredientes', 'Ingrediente', 'IngredienteForm', 'lista_ingredientes.html'],
        'sabores': ['Sabores', 'Sabor', 'SaborForm', 'lista_generica.html'],
        'texturas': ['Texturas', 'Textura', 'TexturaForm', 'lista_generica.html'],
        'tecnicas': ['Técnicas', 'Tecnica', 'TecnicaForm', 'lista_generica.html'],
        'tipos-corte': ['Tipos de Corte', 'TiposCorte', 'TipoCorteForm', 'lista_generica.html'],
        'tipos-ingrediente': ['Tipos de Ingrediente', 'TipoIngrediente', 'TipoIngredienteForm', 'lista_generica.html'],
        'categorias-ingrediente': ['Categorías de Ingrediente', 'CategoriaIngrediente', '', 'lista_generica.html']
    }

    return ents.get(e, "null")

def elementos(request, url):
    e = entidad(url)
    lista = eval(e[1]).objects.all()

    paginator = Paginator(lista, 10)
    page = request.GET.get('page')

    context = {'entidad': e[0], 'elemento_entidad': url, 'lista': paginator.get_page(page)}
    return render(request, 'recetas/' + e[3], context)

def elemento_nuevo(request, url):
    e = entidad(url)

    if request.method == 'POST':
        #form = eval(e[2])(request.POST)
        form = modelform_factory(
            eval(e[1]), 
            fields = '__all__', 
            labels = {'tnombre': 'Nombre', 'csabor': 'Sabor', 'ctextura': 'Textura'},)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Elemento registrado.")
            return HttpResponseRedirect("/e/" + url)

    else:
        form = modelform_factory(eval(e[1]), fields = '__all__', labels = {'tnombre': 'Nombre'},)
        # form = eval(e[2])(label_suffix="")
            
    return render(request, 'recetas/form_generico.html', {'form': form})

def elemento_edit(request, url, cid):
    e = entidad(url)

    if request.method == 'POST':
        instance = get_object_or_404(eval(e[1]), cid = cid)
        form = eval(e[2])(request.POST or None, instance = instance)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Elemento actualizado.")
            return HttpResponseRedirect("/e/" + url)

    else:
        instance = get_object_or_404(eval(e[1]), cid = cid)
        form = eval(e[2])(request.POST or None, instance=instance, label_suffix="")

    return render(request, 'recetas/form_generico.html', {'form': form})

def elemento_del(request, url, cid):
    e = entidad(url)
    elemento = get_object_or_404(eval(e[1]), cid = cid)
    elemento.delete()
    messages.add_message(request, messages.SUCCESS, "Elemento eliminado.")
    return HttpResponseRedirect("/e/" + url)
