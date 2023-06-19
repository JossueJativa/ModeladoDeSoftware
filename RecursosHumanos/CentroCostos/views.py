from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Usuarios?usuario="+username+"&password="+password)
            data = url.json()
        except:
            return render(request, 'exception.html', {
                'message': "Usuario o contraseña incorrectos"
            })

        if data[0]['OBSERVACION'] == "INGRESO EXITOSO":

            url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
            data = url.json()

            return render(request, 'centrocostos.html',{
                'data': data
            })
    else:
        return render(request, 'login.html')
    