from django.db import models

# Create your models here.

class Parroquia(models.Model):
    
    class Meta:       
        verbose_name_plural = "Parroquias"
    
    opciones_tipo_parroquia = (
        ('rural','Parroquia rural'),
        ('urbana','Parroquia urbana'),
        )

    nombre = models.CharField(max_length=60)   
    tipo_parroquia = models.CharField(max_length=30, \
            choices=opciones_tipo_parroquia) 

    def __str__(self):
        return "%s - %s" % (self.nombre, 
                self.tipo_parroquia)


class Barrio(models.Model):          
        
    opciones_parques = (
        (1,'Un Parque'),
        (2,'Dos Parques'),
        (3,'Dos Parques'),
        (4,'Dos Parques'),
        (5,'Dos Parques'),
        (6,'Dos Parques'),       
        )

    nombre = models.CharField(max_length=60) 
    viviendas = models.IntegerField("numero de viviendas")
    parques = models.IntegerField("numero de parques", choices=opciones_parques)
    edificios = models.IntegerField("numero de edificios")
    parroquia = models.ForeignKey(Parroquia, related_name='lasparroquias', 
            on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %d - %d - %d - %s" % (self.nombre, 
                self.viviendas,
                self.parques,
                self.edificios,
                self.parroquia)

