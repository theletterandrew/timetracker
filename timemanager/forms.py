from django.forms import ModelForm
from timemanager.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

    form = ProjectForm()
    
