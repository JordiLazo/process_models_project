from django.forms import ModelForm, forms
from .models import Academia, CiudadesAcademia


class AcademiaForm(ModelForm):
    class Meta:
        model = Academia

class CiudadAcademiaForm(ModelForm):
    class Meta:
        model = CiudadesAcademia