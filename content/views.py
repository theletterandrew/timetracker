from django.shortcuts import render

def home(request):
    return render(request, 'content/home.html')

def docs(request):
    return render(request, 'content/docs.html')
