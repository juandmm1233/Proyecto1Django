from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('programas/', views.programa_lista, name='programa_lista'),
    path('programas/nuevo/', views.programa_crear, name='programa_crear'),
    path('programas/<int:pk>/', views.programa_detalle, name='programa_detalle'),
    path('cursos/', views.curso_lista, name='curso_lista'),
    path('cursos/nuevo/', views.curso_crear, name='curso_crear'),
    path('cursos/<int:pk>/', views.curso_detalle, name='curso_detalle'),
    path('cursos/<int:curso_pk>/inscribir/', views.inscripcion_crear_curso, name='inscripcion_crear_curso'),
    path('estudiantes/', views.estudiante_lista, name='estudiante_lista'),
    path('estudiantes/nuevo/', views.estudiante_crear, name='estudiante_crear'),
    path('estudiantes/<int:pk>/', views.estudiante_detalle, name='estudiante_detalle'),
    path('estudiantes/<int:estudiante_pk>/inscribir/', views.inscripcion_crear_estudiante, name='inscripcion_crear_estudiante'),
]
