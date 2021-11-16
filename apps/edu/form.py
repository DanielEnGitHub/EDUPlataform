from django import forms
from django.forms import ModelForm
from .models import secciones, alumnos, profesores, materias, clases, horarios, asistencias

class seccionesForm(ModelForm):
    class Meta:
        model = secciones
        fields = [
            'salon',
        ]

        labels = {
            'salon' : 'Seccion',
        }

class alumnosForm(forms.ModelForm):
    class Meta:
        model = alumnos
        fields = [
            'carnet',
            'nombre',
            'apellido',
            'jornada',
            'genero',
            'fecha_nacimiento',
            'telefono',
            'grado',
            'fk_seccion',
        ]

        labels = {
            'carnet' : 'Carnet',
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'jornada' : 'Jornada',
            'genero' : 'Genero',
            'fecha_nacimiento' : 'Fecha de nacimiento',
            'telefono' : 'No. Telefono',
            'grado' : 'Grado',
            'fk_seccion' : 'Seccion',
        }


class profesoresForm(forms.ModelForm):
    class Meta:
        model = profesores
        fields = [
            'carnet',
            'nombre',
            'apellido',
            'dpi',
            'jornada',
            'especialidad',
            'genero',
            'fecha_nacimiento',
            'telefono',
        ]

        labels = {
            'carnet' : 'Carnet',
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'dpi' : 'DPI',
            'jornada' : 'Jornada',
            'especialidad' : 'Especialidad',
            'genero' : 'Genero',
            'fecha_nacimiento' : 'Fecha de nacimiento',
            'telefono' : 'No. Telefono',
        }


class materiasForm(ModelForm):
    class Meta:
        model = materias
        fields = [
            'nombre',
            'descripcion',
        ]

        labels = {
            'nombre' : 'Nombre',
            'descripcion' : 'Descripcion',
        }

class clasesForm(ModelForm):
    class Meta:
        model = clases
        fields = [
            'fk_profesor',
            'fk_materia',
        ]

        labels = {
            'fk_profesor' : 'Profesor',
            'fk_materia' : 'Materia',
        }


class horariosForm(ModelForm):
    class Meta:
        model = horarios
        fields = [
            'fk_clase',
            'fk_seccion',
            'horario_curso',
        ]

        labels = {
            'fk_clase' : 'Clase',
            'fk_seccion' : 'Seccion',
            'horario_curso' : 'Hora',
        }

class asistenciasForm(ModelForm):
    class Meta:
        model = asistencias
        fields = [
            'fk_alumno',
            'fk_clase',
            'asistio',
            'fecha',
        ]

        labels = {
            'fk_alumno' : 'Alumno',
            'fk_clase' : 'Clase',
            'asistio' : 'Asistio',
            'Fecha' : 'Fecha',
        }
