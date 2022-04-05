from django.forms import ModelForm
from .models import Films, Director

class FilmForm(ModelForm):
    class Meta:
        model = Films
        fields = '__all__'

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'