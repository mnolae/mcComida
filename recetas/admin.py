from django.contrib import admin
from .models import *

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('tnombre', )
    search_fields = ('tnombre', )
    
class SaborAdmin(admin.ModelAdmin):
    list_display = ('tnombre', )
    search_fields = ('tnombre', )

class TecnicaAdmin(admin.ModelAdmin):
    list_display = ('tnombre', )
    search_fields = ('tnombre', )

admin.site.register(Ingrediente)
admin.site.register(Sabor,  SaborAdmin)
admin.site.register(Tecnica,  TecnicaAdmin)
admin.site.register(RparcialesRcompuestas)

admin.site.register(CategoriaIngrediente)
admin.site.register(IngredienteInfo)
admin.site.register(IngredientesRecetas)
admin.site.register(RecetasCompuestas)
admin.site.register(RecetasParciales)
admin.site.register(Textura)
admin.site.register(TipoIngrediente)
admin.site.register(TiposCorte)
