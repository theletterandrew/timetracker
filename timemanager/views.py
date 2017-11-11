from django.shortcuts import render

def manager(request):
    args = {'user': request.user}
    return render(request, 'timemanager/manager.html', args)

def add(request):
    args = {'user': request.user}
    return render(request, 'timemanager/add.html', args)
