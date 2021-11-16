from django.shortcuts import render, redirect
from .form import *
from .models import *
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout



#------------------INDEX-------------------------
def index(request):
    return render(request, 'portada.html')


#------------------INICIO-------------------------
def inicio(request):
    if request.user.is_authenticated:
        busqueda = request.GET.get("buscar")

        alumno = alumnos.objects.all()
        profesor = profesores.objects.all()
        materia = materias.objects.all()
        clase = clases.objects.all()
        seccion = secciones.objects.all()
        horario = horarios.objects.all()
        asistencia = asistencias.objects.all()

        if busqueda:
            profesor = profesores.objects.filter(
                Q(nombre__icontains = busqueda) |
                Q(apellido__icontains = busqueda) |
                Q(carnet__icontains = busqueda) |
                Q(dpi__icontains = busqueda) |
                Q(especialidad__icontains = busqueda) |
                Q(jornada__icontains = busqueda) |
                Q(fecha_nacimiento__icontains = busqueda) |
                Q(telefono__icontains = busqueda)
            ).distinct()

        data = {
        'alumno': alumno,
        'profesor': profesor,
        'materia': materia,
        'clase': clase,
        'seccion': seccion,
        'horario': horario,
        'asistencia': asistencia,
        }
        # contenedor = lista.objects.all()
        # data={
        #     'contenedor':contenedor
        return render(request, 'inicio.html', data)
        #     }
    else:
        return redirect('login')

#*****************************************************LOGIN LOGOUT************************************************************************
#-----------------LOGIN-------------------------
def login(request):
    if request.user.is_authenticated:
        alumno = alumnos.objects.all()
        context = {'alumno':alumno}

        return render(request, 'inicio.html', context)
    else:
     # Creamos el formulario de autenticación vacío
        form = AuthenticationForm()
        if request.method == "POST":
            # Añadimos los datos recibidos al formulario
            form = AuthenticationForm(data=request.POST)
            # Si el formulario es válido...
            if form.is_valid():
                # Recuperamos las credenciales validadas
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                # Verificamos las credenciales del usuario
                user = authenticate(username=username, password=password)

                # Si existe un usuario con ese nombre y contraseña
                if user is not None:
                    # Hacemos el login manualmente
                    do_login(request, user)
                    # Y le redireccionamos a la portada
                    return redirect('inicio')

        # Si llegamos al final renderizamos el formulario
        return render(request, "iniciarSesion.html", {'form': form})


#-----------------LOGOUT-------------------------
def logout(request):
     # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

#*****************************************************FIN LOGIN LOGOUT************************************************************************

#*****************************************************SECCION************************************************************************
#------------------AGREGAR SECCION-------------------------
def CrearSecciones(request):
    if request.user.is_authenticated:
        data = {
        'form': seccionesForm()
        }

        if request.method == 'POST':
            formulario = seccionesForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                return redirect('inicio')
        return render(request, 'Secciones/CrearSecciones.html', data)
    else:
        return redirect('login')

#----------------MOSTRAR SECCION-----------------------------
def seccionesShow(request):
   if request.user.is_authenticated:
       seccion = secciones.objects.all()
       context = {'seccion':seccion}
       return render(request, 'Secciones/VerSecciones.html', context)
   else:
       return redirect('login')


#------------------EDITAR SECCION-------------------------
def modificarSecciones(request, id_secciones):
   if request.user.is_authenticated:
       contenedor = secciones.objects.get(id_secciones=id_secciones)
       data={
       'form':seccionesForm(instance=contenedor)
       }

       if request.method == 'POST':
           formulario = seccionesForm(data=request.POST, instance=contenedor)
           if formulario.is_valid():
               formulario.save()
               data['form'] = formulario
               return redirect('inicio')

       return render(request, 'Secciones/EditarSecciones.html', data)
   else:
       return redirect('login')


#------------------ELIMINAR SECCION-------------------------
def eliminarSecciones(request, id_secciones):
   if request.user.is_authenticated:
       contenedor = secciones.objects.get(id_secciones=id_secciones)
       contenedor.delete()

       return redirect('inicio')
   else:
       return redirect('login')

#*****************************************************FIN SECCION************************************************************************


#*****************************************************ALUMNOS************************************************************************
#------------------REGISTRAR ALUMNOS-------------------------
def alumnosCreate(request):
    if request.user.is_authenticated:
        data = {
        'form': alumnosForm(),
        }

        if request.method == 'POST':
            formulario = alumnosForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                return redirect('inicio')
        return render(request, 'Alumno/RegistrarAlumno.html', data)
    else:
        return redirect('login')
 #----------------MOSTRAR ALUMNOS-----------------------------
def alumnosShow(request):
    if request.user.is_authenticated:
        alumno = alumnos.objects.all()
        context = {'alumno':alumno}
        return render(request, 'Alumno/VerAlumnos.html', context)
    else:
        return redirect('login')


#------------------EDITAR ALUMNOS-------------------------
def modificar(request, id_alumnos):
    if request.user.is_authenticated:
        contenedor = alumnos.objects.get(id_alumnos=id_alumnos)
        data={
        'form':alumnosForm(instance=contenedor)
        }

        if request.method == 'POST':
            formulario = alumnosForm(data=request.POST, instance=contenedor)
            if formulario.is_valid():
                formulario.save()
                data['form'] = formulario
                return redirect('inicio')

        return render(request, 'Alumno/EditarAlumno.html', data)
    else:
        return redirect('login')


#------------------ELIMINAR ALUMNOS-------------------------
def eliminar(request, id_alumnos):
    if request.user.is_authenticated:
        contenedor = alumnos.objects.get(id_alumnos=id_alumnos)
        contenedor.delete()

        return redirect('inicio')
    else:
        return redirect('login')
#*****************************************************FIN ALUMNOS************************************************************************


#*****************************************************PROFESORES************************************************************************
#-----------------REGISTRAR PROFESORES-------------------------
def profesoresCreate(request):
    if request.user.is_authenticated:
        data = {
        'form': profesoresForm(),
        }

        if request.method == 'POST':
            formulario = profesoresForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                return redirect('inicio')
        return render(request, 'RegistrarProfesor.html', data)
    else:
        return redirect('login')

#----------------MOSTRAR PROFESORES-----------------------------
def profesoresShow(request):
   if request.user.is_authenticated:
       profesor = profesores.objects.all()
       context = {'profesor':profesor}
       return render(request, 'VerProfesores.html', context)
   else:
       return redirect('login')


#------------------EDITAR PROFESORES-------------------------
def modificarProfesores(request, id_profesores):
   if request.user.is_authenticated:
       contenedor = profesores.objects.get(id_profesores=id_profesores)
       data={
       'form':profesoresForm(instance=contenedor)
       }

       if request.method == 'POST':
           formulario = profesoresForm(data=request.POST, instance=contenedor)
           if formulario.is_valid():
               formulario.save()
               data['form'] = formulario
               return redirect('inicio')

       return render(request, 'EditarProfesores.html', data)
   else:
       return redirect('login')


#------------------ELIMINAR PROFESORES-------------------------
def eliminarProfesores(request, id_profesores):
   if request.user.is_authenticated:
       contenedor = profesores.objects.get(id_profesores=id_profesores)
       contenedor.delete()

       return redirect('inicio')
   else:
       return redirect('login')


#*****************************************************FIN PROFESORES************************************************************************


#*****************************************************MATERIA************************************************************************
#------------------AGREGAR MATERIA-------------------------
def CrearMateria(request):
    if request.user.is_authenticated:
        data = {
        'form': materiasForm()
        }

        if request.method == 'POST':
            formulario = materiasForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                return redirect('inicio')
        return render(request, 'Materia/CrearMateria.html', data)
    else:

        return redirect('login')

#----------------MOSTRAR MATERIA-----------------------------
def materiaShow(request):
   if request.user.is_authenticated:
       materia = materias.objects.all()
       context = {'materia':materia}
       return render(request, 'Materia/VerMateria.html', context)
   else:
       return redirect('login')


#------------------EDITAR MATERIA-------------------------
def modificarMateria(request, id_materias):
   if request.user.is_authenticated:
       contenedor = materias.objects.get(id_materias=id_materias)
       data={
       'form':materiasForm(instance=contenedor)
       }

       if request.method == 'POST':
           formulario = materiasForm(data=request.POST, instance=contenedor)
           if formulario.is_valid():
               formulario.save()
               data['form'] = formulario
               return redirect('inicio')

       return render(request, 'Materia/EditarMateria.html', data)
   else:
       return redirect('login')


#------------------ELIMINAR MATERIA-------------------------
def eliminarMateria(request, id_materias):
   if request.user.is_authenticated:
       contenedor = materias.objects.get(id_materias=id_materias)
       contenedor.delete()

       return redirect('inicio')
   else:
       return redirect('login')

#*****************************************************FIN MATERIA************************************************************************



#*****************************************************CLASE************************************************************************
#------------------AGREGAR CLASE-------------------------
def crearClase(request):
    if request.user.is_authenticated:
        data = {
        'form': clasesForm()
        }

        if request.method == 'POST':
            formulario = clasesForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                return redirect('inicio')
        return render(request, 'Clase/CrearClase.html', data)
    else:
        return redirect('login')

#----------------MOSTRAR CLASE-----------------------------
def claseShow(request):
   if request.user.is_authenticated:
       clase = clases.objects.all()
       context = {'clase':clase}
       return render(request, 'Clase/VerClase.html', context)
   else:
       return redirect('login')


#------------------EDITAR CLASE-------------------------
def modificarClase(request, id_clases):
   if request.user.is_authenticated:
       contenedor = clases.objects.get(id_clases=id_clases)
       data={
       'form':clasesForm(instance=contenedor)
       }

       if request.method == 'POST':
           formulario = clasesForm(data=request.POST, instance=contenedor)
           if formulario.is_valid():
               formulario.save()
               data['form'] = formulario
               return redirect('inicio')

       return render(request, 'Clase/EditarClase.html', data)
   else:
       return redirect('login')


#------------------ELIMINAR CLASE-------------------------
def eliminarClase(request, id_clases):
   if request.user.is_authenticated:
       contenedor = clases.objects.get(id_clases=id_clases)
       contenedor.delete()

       return redirect('inicio')
   else:
       return redirect('login')

#*****************************************************FIN CLASE************************************************************************













#*****************************************************HORARIO************************************************************************
#------------------AGREGAR HORARIO-------------------------
def crearHorario(request):
    if request.user.is_authenticated:
        data = {
        'form': horariosForm()
        }

        if request.method == 'POST':
            formulario = horariosForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                return redirect('inicio')
        return render(request, 'Horario/crearHorario.html', data)
    else:
        return redirect('login')

#----------------MOSTRAR HORARIO-----------------------------
def horarioShow(request):
   if request.user.is_authenticated:
       horario = horarios.objects.all()
       context = {'horario':horario}
       return render(request, 'Horario/VerHorario.html', context)
   else:
       return redirect('login')


#------------------EDITAR HORARIO-------------------------
def modificarHorario(request, id_horarios):
   if request.user.is_authenticated:
       contenedor = horarios.objects.get(id_horarios=id_horarios)
       data={
       'form':horariosForm(instance=contenedor)
       }

       if request.method == 'POST':
           formulario = horariosForm(data=request.POST, instance=contenedor)
           if formulario.is_valid():
               formulario.save()
               data['form'] = formulario
               return redirect('inicio')

       return render(request, 'Horario/EditarHorario.html', data)
   else:
       return redirect('login')


#------------------ELIMINAR HORARIO-------------------------
def eliminarHorario(request, id_horarios):
   if request.user.is_authenticated:
       contenedor = horarios.objects.get(id_horarios=id_horarios)
       contenedor.delete()

       return redirect('inicio')
   else:
       return redirect('login')

#*****************************************************FIN HORARIO************************************************************************












#*****************************************************ASISTENCIA************************************************************************
#------------------AGREGAR ASISTENCIA-------------------------
def crearAsistencia(request):
    if request.user.is_authenticated:
        data = {
        'form': asistenciasForm()
        }

        if request.method == 'POST':
            formulario = asistenciasForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                return redirect('inicio')
        return render(request, 'Asistencia/crearAsistencia.html', data)
    else:
        return redirect('login')

#----------------MOSTRAR ASISTENCIA-----------------------------
def asistenciaShow(request):
   if request.user.is_authenticated:
       asistencia = asistencias.objects.all()
       context = {'asistencia':asistencia}
       return render(request, 'Asistencia/VerAsistencia.html', context)
   else:
       return redirect('login')


#------------------EDITAR ASISTENCIA-------------------------
def modificarAsistencia(request, id_asistencias):
   if request.user.is_authenticated:
       contenedor = asistencias.objects.get(id_asistencias=id_asistencias)
       data={
       'form':asistenciasForm(instance=contenedor)
       }

       if request.method == 'POST':
           formulario = asistenciasForm(data=request.POST, instance=contenedor)
           if formulario.is_valid():
               formulario.save()
               data['form'] = formulario
               return redirect('inicio')

       return render(request, 'Asistencia/EditarAsitencia.html', data)
   else:
       return redirect('login')


#------------------ELIMINAR ASISTENCIA-------------------------
def eliminarAsistencia(request, id_asistencias):
   if request.user.is_authenticated:
       contenedor = asistencias.objects.get(id_asistencias=id_asistencias)
       contenedor.delete()

       return redirect('inicio')
   else:
       return redirect('login')

#*****************************************************FIN ASISTENCIA************************************************************************
