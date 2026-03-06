from django import forms
from .models import Programa, Curso, Estudiante, Inscripcion


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ['nombre', 'codigo', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['programa', 'nombre', 'codigo', 'creditos']


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'codigo', 'email']


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['estudiante', 'curso']

    def clean(self):
        cleaned = super().clean()
        estudiante = cleaned.get('estudiante')
        curso = cleaned.get('curso')
        if estudiante and curso and Inscripcion.objects.filter(estudiante=estudiante, curso=curso).exists():
            raise forms.ValidationError('Este estudiante ya está inscrito en este curso.')
        return cleaned


class InscripcionCursoForm(forms.Form):
    """Solo selecciona estudiante (el curso viene del contexto)."""
    estudiante = forms.ModelChoiceField(queryset=Estudiante.objects.all(), label='Estudiante')


class InscripcionEstudianteForm(forms.Form):
    """Solo selecciona curso (el estudiante viene del contexto)."""
    curso = forms.ModelChoiceField(queryset=Curso.objects.select_related('programa').all(), label='Curso')
