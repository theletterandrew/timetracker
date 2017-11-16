from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Project
from timemanager.forms import ProjectForm


def manager(request):
    projects = Project.objects.filter(user=request.user)
    args = {'user': request.user, 'projects': projects}
    return render(request, 'timemanager/manager.html', args)

def add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            proj = form.save()
            proj.user = request.user
            proj.save()

            return redirect('timemanager:manager')
    else:
        form = ProjectForm()
    args = {'form': form}
    return render(request, 'timemanager/add.html', args)

def viewProject(request, project_id):
    project = Project.objects.filter(pk=project_id)
    return render(request, 'timemanager/view_project.html', {'project': project})
