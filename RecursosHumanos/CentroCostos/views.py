from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    url2 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/GetEmisor")
    data2 = url2.json()
    return render(request, 'index.html',{
        'emisores': data2,
    })

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        emisor = request.POST['emisor']

        try:
            url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Usuarios?usuario="+username+"&password="+password)
            data = url.json()
        except:
            return render(request, 'exception.html', {
                'message': "Usuario o contraseña incorrectos"
            })

        if data[0]['OBSERVACION'] == "INGRESO EXITOSO":
            if emisor == data[0]['NOMBREEMISOR'].strip():
                url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
                data = url.json()

                return render(request, 'centrocostos.html',{
                    'data': data,
                })   
            else:
                return render(request, 'exception.html', {
                    'message': "Emisor mal registrado"
                })
        else:
            return render(request, 'exception.html', {
                'message': "Usuario o contraseña incorrectos"
            })  
    else:
        return render(request, 'exception.html',{
            'message': "Usuario o contraseña incorrectos"
        })
    

def pushCentroCostos (request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']

        try:
            url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosInsert?codigocentrocostos="+codigo+"&descripcioncentrocostos="+descripcion)
            data = url.json()
        except:
            return render(request, 'exception.html', {
                'message': "Error al insertar el centro de costos"
            })
        
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
        data = url.json()
        return render(request, 'centrocostos.html',{
                'data': data,
            })
    else:
        return render(request, 'addCentroDeCostos.html')
    
def agregar(request):
    return render(request, 'agregar.html')

def elimAtributo(request, id, descripcion):
    if request.method == 'POST':
        try:
            url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosDelete?codigocentrocostos="+id+"&descripcioncentrocostos="+descripcion)
        except:
            return render(request, 'exception.html', {
                'message': "Error al eliminar el centro de costos"
            })
        
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
        data = url.json()
        return render(request, 'centrocostos.html',{
                'data': data,
            })
    else:
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
        data = url.json()
        return render(request, 'centrocostos.html',{
                'data': data,
            })
    
def edit(request, id):
    if request.method == "POST":
        descripcion = request.POST['descripcion']

        try:
            url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosUpdate?codigocentrocostos="+id+"&descripcioncentrocostos="+descripcion)

        except:
            return render(request, 'exception.html', {
                'message': "Error al editar el centro de costos"
            })
        
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
        data = url.json()
        return render(request, 'centrocostos.html',{
                'data': data,
            })
    else:
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
        data = url.json()
        return render(request, 'centrocostos.html',{
                'data': data,
            })
    
def editCentroCostos(request, id):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
    data = url.json()

    for datos in data:
        if datos['Codigo'] == int(id):
            data = datos
    
    return render(request, 'editCentroCostos.html',{
        'data': data,
    })

def search(request):
    if request.method == "POST":
        descripcion = request.POST['descripcion']

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSearch?descripcioncentrocostos="+descripcion)
        data = url.json()

        codigo = data[0]['Codigo']
        descripcionmostrar = data[0]['NombreCentroCostos']
        
        return render(request, 'busqueda.html',{
            'codigo': codigo,
            'descripcion': descripcionmostrar,
        })
    else:
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
        data = url.json()
        return render(request, 'centrocostos.html',{
                'data': data,
            })

def PagCentroCostos(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
    data = url.json()
    return render(request, 'centrocostos.html',{
        'data': data,
    })   