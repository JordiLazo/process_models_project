from django import forms
from academyApp.models import AcademiaReview


class FormularioAlumno(forms.ModelForm):
    class Meta:
        model = AcademiaReview
        fields = '__all__'
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}