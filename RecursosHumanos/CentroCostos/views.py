from django.shortcuts import render
import requests

from .models import usuarios

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == "5001" and password == "5001U":
            return render(request, 'index.html')
        else:
            return render(request, 'exception.html', {
                "message": "Usuario o contraseña incorrectos"
            })
    else:
        return render(request, 'login.html')
    
def get_usuarios(request, params={}):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/swagger/index.html/Usuarios", params=params)

    if url.status_code == 200:
        url = url.json()
    else:
        return render(request, 'exception.html', {
            "message": "No se pudo conectar con el servidor"
        })
    
    for i in url:
        usuario = usuarios(username=i['usuario'], password=i['password'])
        usuario.save()

def tables (request):
    usuario = usuarios.objects.all()
    return render(request, 'tables.html', {
        "usuario": usuario
    })