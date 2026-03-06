from django.shortcuts import render, get_object_or_404, redirect
from .models import Programa, Curso, Estudiante, Inscripcion
from .forms import ProgramaForm, CursoForm, EstudianteForm, InscripcionCursoForm, InscripcionEstudianteForm


def index(request):
    """Página de inicio con enlaces a las secciones."""
    return render(request, 'academico/index.html')


def programa_lista(request):
    """Lista de todos los programas."""
    programas = Programa.objects.all()
    return render(request, 'academico/programa_lista.html', {'programas': programas})


def programa_detalle(request, pk):
    """Detalle de un programa con sus cursos."""
    programa = get_object_or_404(Programa, pk=pk)
    return render(request, 'academico/programa_detalle.html', {'programa': programa})


def curso_lista(request):
    """Lista de todos los cursos."""
    cursos = Curso.objects.select_related('programa').all()
    return render(request, 'academico/curso_lista.html', {'cursos': cursos})


def curso_detalle(request, pk):
    """Detalle de un curso con estudiantes inscritos."""
    curso = get_object_or_404(Curso.objects.select_related('programa'), pk=pk)
    inscripciones = curso.inscripciones.select_related('estudiante').all()
    return render(request, 'academico/curso_detalle.html', {
        'curso': curso,
        'inscripciones': inscripciones,
    })


def estudiante_lista(request):
    """Lista de todos los estudiantes."""
    estudiantes = Estudiante.objects.all()
    return render(request, 'academico/estudiante_lista.html', {'estudiantes': estudiantes})


def estudiante_detalle(request, pk):
    """Detalle de un estudiante con sus inscripciones (cursos)."""
    estudiante = get_object_or_404(Estudiante, pk=pk)
    inscripciones = estudiante.inscripciones.select_related('curso', 'curso__programa').all()
    return render(request, 'academico/estudiante_detalle.html', {
        'estudiante': estudiante,
        'inscripciones': inscripciones,
    })


def programa_crear(request):
    """Crear nuevo programa."""
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programa_lista')
    else:
        form = ProgramaForm()
    return render(request, 'academico/form_generico.html', {'form': form, 'titulo': 'Nuevo programa'})


def curso_crear(request):
    """Crear nuevo curso. Opcionalmente pre-seleccionar programa por ?programa=<pk>."""
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_lista')
    else:
        initial = {}
        programa_pk = request.GET.get('programa')
        if programa_pk:
            programa = get_object_or_404(Programa, pk=programa_pk)
            initial['programa'] = programa
        form = CursoForm(initial=initial)
    return render(request, 'academico/form_generico.html', {'form': form, 'titulo': 'Nuevo curso'})


def estudiante_crear(request):
    """Crear nuevo estudiante."""
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiante_lista')
    else:
        form = EstudianteForm()
    return render(request, 'academico/form_generico.html', {'form': form, 'titulo': 'Nuevo estudiante'})


def inscripcion_crear_curso(request, curso_pk):
    """Inscribir estudiante en un curso (desde detalle del curso)."""
    curso = get_object_or_404(Curso, pk=curso_pk)
    if request.method == 'POST':
        form = InscripcionCursoForm(request.POST)
        if form.is_valid():
            estudiante = form.cleaned_data['estudiante']
            if Inscripcion.objects.filter(estudiante=estudiante, curso=curso).exists():
                form.add_error('estudiante', 'Este estudiante ya está inscrito en este curso.')
            else:
                Inscripcion.objects.create(estudiante=estudiante, curso=curso)
                return redirect('curso_detalle', pk=curso_pk)
    else:
        form = InscripcionCursoForm()
    return render(request, 'academico/form_generico.html', {
        'form': form,
        'titulo': f'Inscribir estudiante en {curso.nombre}',
    })


def inscripcion_crear_estudiante(request, estudiante_pk):
    """Inscribir estudiante en un curso (desde detalle del estudiante)."""
    estudiante = get_object_or_404(Estudiante, pk=estudiante_pk)
    if request.method == 'POST':
        form = InscripcionEstudianteForm(request.POST)
        if form.is_valid():
            curso = form.cleaned_data['curso']
            if Inscripcion.objects.filter(estudiante=estudiante, curso=curso).exists():
                form.add_error('curso', 'Este estudiante ya está inscrito en este curso.')
            else:
                Inscripcion.objects.create(estudiante=estudiante, curso=curso)
                return redirect('estudiante_detalle', pk=estudiante_pk)
    else:
        form = InscripcionEstudianteForm()
    return render(request, 'academico/form_generico.html', {
        'form': form,
        'titulo': f'Inscribir a {estudiante.apellido}, {estudiante.nombre} en un curso',
    })
