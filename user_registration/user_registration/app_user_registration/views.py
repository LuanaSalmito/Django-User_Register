from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        new_user = Usuario()
        new_user.nome = request.POST.get('nome')
        new_user.idade = request.POST.get('idade')
        new_user.save()

    usuarios = {
        'usuarios': Usuario.objects.all()  # Correção: objects em vez de object
    }
    return render(request, 'usuarios/usuarios.html', usuarios)