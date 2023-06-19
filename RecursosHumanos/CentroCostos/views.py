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
    

def pushCentroCostos (request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']

        try:
            url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosInsert?codigocentrocostos="+codigo+"&descripcioncentrocostos="+descripcion)
        except:
            return render(request, 'exception.html', {
                'message': "Error al insertar el centro de costos"
            })
        
        return render(request, 'centrocostos.html',{
                'message': "Se realizo el envio exitosamente"
            })
    else:
        return render(request, 'addCentroDeCostos.html')
    
def pagCentroCostosadd (request):
    return render(request, 'addCentroDeCostos.html')