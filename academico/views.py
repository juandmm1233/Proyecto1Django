from django.shortcuts import render, get_object_or_404
from .models import Programa, Curso, Estudiante


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
