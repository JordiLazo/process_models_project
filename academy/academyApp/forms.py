from django.forms import ModelForm
from .models import Academia


class AcademiaForm(ModelForm):
    class Meta:
        model = Academia

