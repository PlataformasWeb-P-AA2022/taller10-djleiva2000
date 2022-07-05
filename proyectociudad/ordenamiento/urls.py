"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from.import views


urlpatterns = [
    path('', views.index, name='index'),
        # Urls para Parroquias
    path('parroquia/<int:id>', views.obtenerParroquia, name='obtenerParroquia'),
    path('crear/parroquia', views.crearParroquia, name='crearParroquia'),       
    path('editar/parroquia/<int:id>', views.editarParroquia, name='editarParroquia'),     
        
        # Urls para Barrios   
    path('crear/barrioParroquia/<int:id>', views.crearBarrioParroquia, name='crearBarrioParroquia'),        
    path('editar/barrio/<int:id>', views.editarBarrio, name='editarBarrio'),
    path('crear/barrio', views.crearBarrio, name='crearBarrio'),
      
 ]