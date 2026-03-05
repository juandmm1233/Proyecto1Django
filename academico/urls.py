from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('programas/', views.programa_lista, name='programa_lista'),
    path('programas/<int:pk>/', views.programa_detalle, name='programa_detalle'),
    path('cursos/', views.curso_lista, name='curso_lista'),
    path('cursos/<int:pk>/', views.curso_detalle, name='curso_detalle'),
    path('estudiantes/', views.estudiante_lista, name='estudiante_lista'),
    path('estudiantes/<int:pk>/', views.estudiante_detalle, name='estudiante_detalle'),
]
