from django.urls import path
    
from . import views

urlpatterns = [

    # Index    
    path('', views.index, name='index'),

    # Lista de elementos
    path('e/<str:url>', views.elementos, name='elementos'),
    path('e/<str:url>/nuevo', views.elemento_nuevo, name='elemento_nuevo'),
    path('e/<str:url>/editar/<int:cid>', views.elemento_edit, name='elemento_edit'),
    path('e/<str:url>/eliminar/<int:cid>', views.elemento_del, name='elemento_del'),

]
