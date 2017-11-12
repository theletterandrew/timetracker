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
        form = ProjectForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('timemanager:manager')
    else:
        form = ProjectForm(instance=request.user)
        args = {'form': form}
        return render(request, 'timemanager/add.html', args)
