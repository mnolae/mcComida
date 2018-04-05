from django.urls import path, include
    
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('cuenta/', include('django.contrib.auth.urls')),

    # Lista de elementos
    path('e/<str:url>', views.elementos, name='elementos'),
    path('e/<str:url>/nuevo', views.elemento_nuevo, name='elemento_nuevo'),
    path('e/<str:url>/editar/<int:cid>', views.elemento_edit, name='elemento_edit'),
    path('e/<str:url>/eliminar/<int:cid>', views.elemento_del, name='elemento_del'),
    path('e/recetas-simples/ver/<int:cid>', views.recetasimple_show, name='recetasimple_show'),
    path('e/recetas-compuestas/ver/<int:cid>', views.recetacompuesta_show, name='recetacompuesta_show'),
]
