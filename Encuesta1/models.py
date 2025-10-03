from django.db import models

# Create your models here.
#Ola :p 

class Proyecto(models.Model):
    # CÓDIGO COMO PK
    codigo = models.CharField(max_length=20, primary_key=True, verbose_name="CÓDIGO")
    
    # CORREO DEL REPRESENTANTE
    correo_representante = models.EmailField(verbose_name="CORREO DEL REPRESENTANTE")
    
    # MODALIDAD CON OPCIONES EN MAYÚSCULAS
    MODALIDAD_CHOICES = [
        ('TRABAJO DE INVESTIGACIÓN', 'TRABAJO DE INVESTIGACIÓN'),
        ('MATERIALES EDUCATIVOS', 'MATERIALES EDUCATIVOS'),
        ('PROTOTIPO', 'PROTOTIPO'),
        ('REPORTE', 'REPORTE'),
        ('PROYECTOS DE VINCULACIÓN SOCIAL', 'PROYECTOS DE VINCULACIÓN SOCIAL'),
    ]
    modalidad = models.CharField(
        max_length=50,
        choices=MODALIDAD_CHOICES,
        verbose_name="MODALIDAD"
    )
    
    # EVIDENCIA (ARCHIVO)
    evidencia = models.FileField(upload_to='evidencias/', verbose_name="SUBE TU EVIDENCIA")
    
    def __str__(self):
        return f"{self.codigo} - {self.modalidad}"

