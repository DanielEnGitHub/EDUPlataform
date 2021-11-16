from django.db import models

# Create your models here.
class secciones(models.Model):
    id_secciones = models.AutoField(primary_key = True)
    salon = models.CharField(max_length = 150, blank = False)

    def __str__(self):
        return self.salon

class alumnos(models.Model):
    id_alumnos = models.AutoField(primary_key = True)
    carnet = models.CharField(max_length = 7, blank = False)
    nombre = models.CharField(max_length = 150, blank = False)
    apellido = models.CharField(max_length = 150, blank = False)
    jornada = models.CharField(max_length = 10, blank = False)
    genero = models.CharField(max_length = 10, blank = False)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length = 12, blank = False)
    grado = models.CharField(max_length = 12, blank = False)
    fk_seccion = models.ForeignKey('secciones', on_delete=models.SET_NULL,blank=True,null=True)



class profesores(models.Model):
    id_profesores = models.AutoField(primary_key = True)
    carnet = models.CharField(max_length = 7, blank = False)
    nombre = models.CharField(max_length = 150, blank = False)
    apellido = models.CharField(max_length = 150, blank = False)
    dpi = models.CharField(max_length = 20, blank = False)
    jornada = models.CharField(max_length = 10, blank = False)
    especialidad = models.CharField(max_length = 150, blank = False)
    genero = models.CharField(max_length = 10, blank = False)
    fecha_nacimiento = models.DateField(blank=False)
    telefono = models.CharField(max_length = 12, blank = False)

    def __str__(self):
        return self.apellido

class materias(models.Model):
    id_materias = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50, blank = False)
    descripcion = models.CharField(max_length = 250, blank = False)

    def __str__(self):
        return self.nombre

class clases(models.Model):
    id_clases = models.AutoField(primary_key = True)
    fk_profesor = models.ForeignKey('profesores', on_delete=models.SET_NULL,blank=True,null=True)
    fk_materia = models.ForeignKey('materias', on_delete=models.SET_NULL,blank=True,null=True)

class horarios(models.Model):
    id_horarios = models.AutoField(primary_key = True)
    fk_clase = models.ForeignKey('clases', on_delete=models.SET_NULL,blank=True,null=True)
    fk_seccion = models.ForeignKey('secciones', on_delete=models.SET_NULL,blank=True,null=True)
    horario_curso = models.CharField(max_length = 30, blank = False)

    def __str__(self):
        return self.horario_curso

class asistencias(models.Model):
    id_asistencias = models.AutoField(primary_key = True)
    fk_alumno = models.ForeignKey('alumnos', on_delete=models.SET_NULL,blank=True,null=True)
    fk_clase = models.ForeignKey('clases', on_delete=models.SET_NULL,blank=True,null=True)
    asistio = models.CharField(max_length = 30, blank = False)
    fecha = models.DateField(blank=False)

    def __str__(self):
        return self.asistio
