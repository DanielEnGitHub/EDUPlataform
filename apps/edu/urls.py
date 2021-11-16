from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('', index, name = 'index'),
    path('login',login, name="login"),
    path('logout', logout, name = 'logout'),
    path('inicio', inicio, name = 'inicio'),

    #-----ALUMNOS--------
    path('Alumnos', alumnosCreate, name = 'Alumnos'),
    path('modificar/<id_alumnos>/', modificar, name = 'modificar'),
    path('eliminar/<id_alumnos>/', eliminar, name = 'eliminar'),
    #-----FIN ALUMNOS--------


    #-----PROFESORES---------
    path('Profesor', profesoresCreate, name = 'Porfesor'),
    path('VerProfesores', profesoresShow, name = 'VerProfesores'),
    path('modificarProfesores/<id_profesores>/', modificarProfesores, name = 'modificarProfesores'),
    path('eliminarProfesores/<id_profesores>/', eliminarProfesores, name = 'eliminarProfesores'),
    #-----FIN PROFESORES---------


    #-----SECCIONES---------
    path('Secciones', CrearSecciones, name = 'Secciones'),
    path('verSecciones', seccionesShow, name = 'verSecciones'),
    path('modificarSecciones/<id_secciones>/', modificarSecciones, name = 'modificarSecciones'),
    path('eliminarSecciones/<id_secciones>/', eliminarSecciones, name = 'eliminarSecciones'),
    #-----FIN SECCIONES---------

    #-----MATERIAS---------
    path('Materias', CrearMateria, name = 'Materias'),
    path('verMaterias', materiaShow, name = 'verMaterias'),
    path('modificarMateria/<id_materias>/', modificarMateria, name = 'modificarMateria'),
    path('eliminarMateria/<id_materias>/', eliminarMateria, name = 'eliminarMaterias'),
    #-----FIN MATERIAS---------

    #-----CLASE---------
    path('Clase', crearClase, name = 'Clase'),
    path('verClase', claseShow, name = 'verClase'),
    path('modificarClase/<id_clases>/', modificarClase, name = 'modificarClase'),
    path('eliminarClase/<id_clases>/', eliminarClase, name = 'eliminarClase'),
    #-----FIN CLASE---------

    #-----HORARIO---------
    path('Horario', crearHorario, name = 'Horario'),
    path('VerHorario', horarioShow, name = 'VerHorario'),
    path('modificarHorario/<id_horarios>/', modificarHorario, name = 'modificarHorario'),
    path('eliminarHorario/<id_horarios>/', eliminarHorario, name = 'eliminarHorario'),
    #-----FIN HORARIO---------

    #-----ASISTENCIA---------
    path('Asistencia', crearAsistencia, name = 'Asistencia'),
    path('VerAsistencia', asistenciaShow, name = 'VerAsistencia'),
    path('modificarAsistencia/<id_asistencias>/', modificarAsistencia, name = 'modificarAsistencia'),
    path('eliminarAsistencia/<id_asistencias>/', eliminarAsistencia, name = 'eliminarAsistencia'),
    #-----FIN ASISTENCIA---------
]
