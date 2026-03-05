from django.contrib import admin
from .models import Programa, Curso, Estudiante, Inscripcion


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('nombre', 'codigo')


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'programa', 'creditos')
    list_filter = ('programa',)
    search_fields = ('nombre', 'codigo')


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'apellido', 'nombre', 'email')
    search_fields = ('nombre', 'apellido', 'codigo')


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'fecha_inscripcion')
    list_filter = ('curso',)
    search_fields = ('estudiante__nombre', 'estudiante__apellido', 'curso__nombre')
