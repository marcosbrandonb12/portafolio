from django.shortcuts import render
from .models import Project, Portfolio

def home(request):
    projects = Project.objects.all()
    perfil = Portfolio.objects.first()
    return render(request, 'home.html', {'projects': projects, 'perfil': perfil})

