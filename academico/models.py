from django.db import models


class Programa(models.Model):
    """Programa académico (ej: Ingeniería de Sistemas, Derecho)."""
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Curso(models.Model):
    """Curso que pertenece a un programa."""
    programa = models.ForeignKey(
        Programa,
        on_delete=models.CASCADE,
        related_name='cursos'
    )
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20)
    creditos = models.PositiveSmallIntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['programa', 'codigo']
        unique_together = [['programa', 'codigo']]
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Estudiante(models.Model):
    """Estudiante que puede inscribirse a varios cursos."""
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    codigo = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return f"{self.codigo} - {self.apellido}, {self.nombre}"


class Inscripcion(models.Model):
    """Matrícula/inscripción: relación estudiante-curso (única por pareja)."""
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_inscripcion']
        unique_together = [['estudiante', 'curso']]
        verbose_name = 'Inscripción'
        verbose_name_plural = 'Inscripciones'

    def __str__(self):
        return f"{self.estudiante} en {self.curso}"
