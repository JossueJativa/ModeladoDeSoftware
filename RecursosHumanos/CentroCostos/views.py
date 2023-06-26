from django.shortcuts import render
from django.urls import reverse
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
            return render(request, 'exceptiondentro.html', {
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
            return render(request, 'exceptiondentro.html', {
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
            return render(request, 'exceptiondentro.html', {
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

def PagMovimientoPlanilla (request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSelect")
    data = url.json()

    ##Filtrar por prioridad
    data = sorted(data, key=lambda k: k['Prioridad'], reverse=True)

    return render(request, 'movimientoplanilla.html',{
        'data': data,
    })

def PagMovimientoPlanillaSearch (request):
    if request.method == "POST":
        ## buscar por Concepto
        concepto = request.POST['Concepto']
        ##Quitar los espacios entre palabras
        concepto = concepto.replace(" ", "&")

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSearch?Concepto="+concepto)
        data = url.json()

        ##Filtrar por prioridad
        data = sorted(data, key=lambda k: k['Prioridad'], reverse=True)
        
        return render(request, 'busquedaMovimientoPlantilla.html',{
            'data': data,
        })
    
def eliminarMovimientoPlanilla (request, id):
    if request.method == 'POST':

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSelect")
        data = url.json()

        #Filter by priority
        data = sorted(data, key=lambda k: k['Prioridad'], reverse=True)

        # buscar por Concepto
        for datos in data:
            if datos['CodigoConcepto'] == int(id):
                concepto = datos['Concepto']
                ##Quitar los espacios entre palabras
                concepto = concepto.replace(" ", "&")

        try:
            url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimeintoPlanillaDelete?codigomovimiento="+id+
                               "&descripcionomovimiento="+concepto)
            data = url.json()
        except:
            return render(request, 'exceptiondentro.html', {
                'message': "Error al eliminar el movimiento de planilla"
            })
        
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSelect")
        data = url.json()

        ##Filtrar por prioridad
        data = sorted(data, key=lambda k: k['Prioridad'], reverse=True)

        return render(request, 'movimientoplanilla.html',{
                'data': data,
            })

    
def PagMovimientoPlanillaEdit (request, id):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSelect")
    data = url.json()

    for datos in data:
        if datos['CodigoConcepto'] == int(id):
            data = datos

    ##Sacar tipos de operaciones
    url2 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoOperacion")
    data2 = url2.json()

    ##Sacar movimiento excepcion
    url3 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientosExcepcion1y2")
    data3 = url3.json()

    #Sacar movimiento de excepcion 3
    url4 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientosExcepcion3")
    data4 = url4.json()

    ##Sacar traba aplica a iess
    url5 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabaAfectaIESS")
    data5 = url5.json()

    ##Sacar afecta impuesto a la renta
    url6 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabAfecImpuestoRenta")
    data6 = url6.json()
    
    return render(request, 'editMovimientoPlanilla.html',{
        'datos': data,
        'operacion': data2,
        'excepcion': data3,
        'excepcion3': data4,
        'traba': data5,
        'afecta': data6,
    })

def editMovimientoPlantilla (request, id):
    if request.method == "POST":
        Conceptos = request.POST['Conceptos']
        Prioridad = request.POST['Prioridad']
        TipoOperacion = request.POST['TipoOperacion']
        Cuenta1 = request.POST['Cuenta1']
        Cuenta2 = request.POST['Cuenta2']
        Cuenta3 = request.POST['Cuenta3']
        Cuenta4 = request.POST['Cuenta4']
        MovimientoExcepcion1 = request.POST['MovimientoExcepcion1']
        MovimientoExcepcion2 = request.POST['MovimientoExcepcion2']
        MovimientoExcepcion3 = request.POST['MovimientoExcepcion3']
        Traba_Aplica_iess = request.POST['Traba_Aplica_iess']
        Traba_Proyecto_imp_renta = request.POST['Traba_Proyecto_imp_renta']
        Aplica_Proy_Renta = request.POST['Aplica_Proy_Renta']
        Empresa_Afecta_Iess = request.POST['Empresa_Afecta_Iess']

        try:
            requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaUpdate?codigoplanilla="+id+"&conceptos="+Conceptos+"&prioridad="+Prioridad+"&tipooperacion="+TipoOperacion+"&cuenta1="+Cuenta1+"&cuenta2="+Cuenta2+"&cuenta3="+Cuenta3+"&cuenta4="+Cuenta4+"&MovimientoExcepcion1="+MovimientoExcepcion1+"&MovimientoExcepcion2="+MovimientoExcepcion2+"&MovimientoExcepcion3="+MovimientoExcepcion3+"&Traba_Aplica_iess="+Traba_Aplica_iess+"&Traba_Proyecto_imp_renta="+Traba_Proyecto_imp_renta+"&Aplica_Proy_Renta="+Aplica_Proy_Renta+"&Empresa_Afecta_Iess="+Empresa_Afecta_Iess)
        except:
            return render(request, 'exceptiondentro.html',{
                'message': 'Error al actualizar el movimiento de planilla',
            })

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSelect")
        data = url.json()

        ##Filtrar por prioridad
        data = sorted(data, key=lambda k: k['Prioridad'], reverse=True)

        return render(request, 'movimientoplanilla.html',{
            'data': data,
        })
    
def PagMovimientoPlanillaCreate (request):
    ##Sacar tipos de operaciones
    url2 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoOperacion")
    data2 = url2.json()

    ##Sacar movimiento excepcion
    url3 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientosExcepcion1y2")
    data3 = url3.json()

    #Sacar movimiento de excepcion 3
    url4 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientosExcepcion3")
    data4 = url4.json()

    ##Sacar traba aplica a iess
    url5 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabaAfectaIESS")
    data5 = url5.json()

    ##Sacar afecta impuesto a la renta
    url6 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabAfecImpuestoRenta")
    data6 = url6.json()

    return render(request, 'agregarMovimiento.html',{
        'operacion': data2,
        'excepcion': data3,
        'excepcion3': data4,
        'traba': data5,
        'afecta': data6,
    })

def pushMovimientoPlantilla(request):
    if request.method == "POST":
        Conceptos = request.POST['Conceptos']
        Prioridad = request.POST['Prioridad']
        TipoOperacion = request.POST['TipoOperacion']
        Cuenta1 = request.POST['Cuenta1']
        Cuenta2 = request.POST['Cuenta2']
        Cuenta3 = request.POST['Cuenta3']
        Cuenta4 = request.POST['Cuenta4']
        MovimientoExcepcion1 = request.POST['MovimientoExcepcion1']
        MovimientoExcepcion2 = request.POST['MovimientoExcepcion2']
        MovimientoExcepcion3 = request.POST['MovimientoExcepcion3']
        Traba_Aplica_iess = request.POST['Traba_Aplica_iess']
        Traba_Proyecto_imp_renta = request.POST['Traba_Proyecto_imp_renta']
        Aplica_Proy_Renta = request.POST['Aplica_Proy_Renta']
        Empresa_Afecta_Iess = request.POST['Empresa_Afecta_Iess']
        
        try:
            requests.post("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaInsert?conceptos="+Conceptos+
                         "&prioridad="+Prioridad+"&tipooperacion="+TipoOperacion+"&cuenta1="+Cuenta1+"&cuenta2="+Cuenta2+
                         "&cuenta3="+Cuenta3+"&cuenta4="+Cuenta4+"&MovimientoExcepcion1="+MovimientoExcepcion1+
                         "&MovimientoExcepcion2="+MovimientoExcepcion2+"&MovimientoExcepcion3="+MovimientoExcepcion3+
                         "&Traba_Aplica_iess="+Traba_Aplica_iess+"&Traba_Proyecto_imp_renta="+Traba_Proyecto_imp_renta+
                         "&Aplica_Proy_Renta="+Aplica_Proy_Renta+"&Empresa_Afecta_Iess="+Empresa_Afecta_Iess)
        except:
            return render(request, 'exceptiondentro.html',{
                'message': 'Error al insertar el movimiento de planilla',
            })

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSelect")
        data = url.json()

        ##Filtrar por prioridad
        data = sorted(data, key=lambda k: k['Prioridad'], reverse=True)

        return render(request, 'movimientoplanilla.html',{
            'data': data,
        }) 

def PagTipoTrabajador(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoTrabajador")
    data = url.json()
    return render(request, 'tipotrabajador.html',{
        'data': data,
    })        