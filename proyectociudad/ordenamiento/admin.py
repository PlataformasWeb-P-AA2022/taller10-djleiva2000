from django.contrib import admin
# Importar las clases del modelo
from ordenamiento.models import Parroquia, Barrio
# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Parroquia
class ParroquiaAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'tipo_parroquia')
    search_fields = ('nombre', 'tipo_parroquia')
   
# admin.site.register se lo altera
# el primer argumento es el modelo (Parroquia)
# el segundo argumento la clase ParroquiaAdmin
admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'viviendas', 'parques','edificios','parroquia')
    search_fields = ('nombre', 'parques')
    
# admin.site.register se lo altera
# el primer argumento es el modelo (Barrio)
# el segundo argumento la clase BarrioAdmin
admin.site.register(Barrio, BarrioAdmin)

