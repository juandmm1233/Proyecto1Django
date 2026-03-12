# Universidad - App académica (Django)

Aplicación Django que modela y visualiza información académica básica de una universidad: **programas**, **cursos** y **estudiantes**, con la relación de matrículas/inscripciones entre estudiantes y cursos.

## Reglas de negocio

- Un **Programa** tiene muchos **Cursos**.
- Un **Curso** pertenece a un **Programa**.
- Un **Estudiante** puede inscribirse a varios **Cursos**.
- Un **Curso** puede tener varios **Estudiantes**.
- La pareja (estudiante, curso) es única en **Inscripción** (no se repite).

## Requisitos

- Python 3.10+
- Django 5+

## Instalación

```bash
# Clonar el repositorio (o estar en la carpeta del proyecto)
git clone <url-de-tu-repo-en-github>
cd 2

# Crear y activar entorno virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
# source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py migrate

# Crear superusuario (opcional, para /admin/)
python manage.py createsuperuser

# Cargar datos de ejemplo (opcional)
python manage.py loaddata academico/fixtures/datos_ejemplo.json

# Ejecutar servidor
python manage.py runserver
```

Abrir en el navegador: **http://127.0.0.1:8000/**

## Estructura de URLs y vistas

| URL | Vista | Descripción |
|-----|--------|-------------|
| `/` | index | Página de inicio |
| `/programas/` | programa_lista | Lista de programas |
| `/programas/<id>/` | programa_detalle | Detalle de programa y sus cursos |
| `/cursos/` | curso_lista | Lista de cursos |
| `/cursos/<id>/` | curso_detalle | Detalle de curso y estudiantes inscritos |
| `/estudiantes/` | estudiante_lista | Lista de estudiantes |
| `/estudiantes/<id>/` | estudiante_detalle | Detalle de estudiante y cursos inscritos |
| `/admin/` | admin | Panel de administración Django |

El **navbar** incluye enlaces a Programas, Cursos y Estudiantes.

## Modelos

- **Programa**: nombre, código, descripción.
- **Curso**: programa (FK), nombre, código, créditos.
- **Estudiante**: nombre, apellido, código, email.
- **Inscripcion**: estudiante (FK), curso (FK), fecha_inscripcion; `unique_together` (estudiante, curso).

## Subir a GitHub

```bash
git add .
git commit -m "App académica: programas, cursos, estudiantes e inscripciones"
# Crear un repositorio nuevo en GitHub y luego:
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git branch -M main
git push -u origin main
```

## Licencia

Uso educativo.

Aportes de Kevin Julian Guerrero Penagos

Kevin se encargó de:

Diseño y estilo (CSS):

Creó todos los archivos CSS dentro de static/css/ para cada sección del proyecto: programas.css, cursos.css, estudiantes.css, index.css, base.css.

Mejoró la apariencia visual de la página, incluyendo colores, tipografía, márgenes y diseño responsivo.

Añadió imágenes y elementos visuales en static/img/ para enriquecer la interfaz (logo, hero, avatar de usuario).

Panel de administración (superusuario):

Configuró un superusuario para Django (admin) para permitir la gestión de Programas, Cursos y Estudiantes de manera fácil.

Esto facilita crear, editar y eliminar registros sin necesidad de modificar directamente la base de datos.

Mejoras en la experiencia de usuario:

Ajustó las plantillas HTML (templates/academico/) para que reflejen correctamente los estilos y sean más intuitivas.

Implementó un flujo más claro en la navegación mediante el navbar y botones de acción visibles.

Gracias a estos aportes, la aplicación no solo funciona correctamente sino que también tiene una interfaz más atractiva y fácil de usar para la gestión académica.