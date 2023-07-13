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
    url2 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/GetEmisor")
    data2 = url2.json()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        emisor = request.POST['emisor']

        if username == "" or password == "" or emisor == "":
            return render(request, 'index.html', {
                'message': "Usuario o contraseña incorrectos",
                'emisores': data2,
            })
        
        #Verificar ingreso de usuario que no ingrese letras
        if username.isalpha() == True:
            return render(request, 'index.html', {
                'message': "Usuario o contraseña incorrectos",
                'emisores': data2,
            })

        try:
            url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Usuarios?usuario="+username+"&password="+password)
            data = url.json()
        except:
            return render(request, 'index.html', {
                'message': "Usuario o contraseña incorrectos",
                'emisores': data2,
            })

        if data[0]['OBSERVACION'] == "INGRESO EXITOSO":
            if emisor == data[0]['NOMBREEMISOR'].strip():
                url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
                data = url.json()

                return render(request, 'centrocostos.html',{
                    'data': data,
                })   
            else:
                return render(request, 'index.html', {
                    'message': "Emisor mal registrado",
                    'emisores': data2,
                })
        else:
            return render(request, 'index.html', {
                'message': "Usuario o contraseña incorrectos",
                'emisores': data2,
            })  
    else:
        return render(request, 'index.html',{
            'message': "Usuario o contraseña incorrectos",
            'emisores': data2,
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

        # buscar por Concepto
        for datos in data:
            if datos['CodigoConcepto'] == int(id):
                concepto = datos['Concepto']

        url = requests.delete("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimeintoPlanillaDelete?codigomovimiento="+id+
                            "&descripcionomovimiento="+concepto)
        
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

        Traba_Aplica_iess = Traba_Aplica_iess + " Aplica"

        if Traba_Proyecto_imp_renta == "Aplica":
            Traba_Proyecto_imp_renta = "Si Aplica"

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

def PagbuscarTrabajadores (request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/GetEmisor")
    dataSucursal = url.json()
    return render(request, 'buscarTrabajador.html', {
        'dataSucursal': dataSucursal,
    })

def PagTrabajadores (request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/GetEmisor")
    dataSucursal = url.json()

    if request.method == "POST":
        ##Buscar la sucursal de la que se quiere sacar los trabajadores
        sucursal = request.POST['sucursal']

        for datos in dataSucursal:
            if datos["NombreEmisor"] == sucursal:
                id = str(datos["Codigo"])

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabajadorSelect?sucursal="+id)
        data = url.json()

        return render(request, 'infoTrabajador.html',{
            'data': data,
            'id': id,
        })

def PagTrabajadoresCreate (request, id):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/GetEmisor")
    dataSucursal = url.json()
    url2 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoTrabajador")
    dataTipoTrabajador = url2.json()
    url3 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/Genero")
    dataGenero = url3.json()
    url4 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/Ocupaciones")
    dataOcupaciones = url4.json()
    url5 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/NivelSalarial")
    dataNivelSalarial = url5.json()
    url6 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoContrato")
    dataTipoContrato = url6.json()
    url7 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoCese")
    dataTipoCese = url7.json()
    url8 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/EstadoCivil")
    dataEstadoCivil = url8.json()
    url9 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoComision")
    dataTipoComision = url9.json()
    url10 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/PeriodoVacaciones")
    dataPeriodoVacaciones = url10.json()
    url11 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/EsReingreso")
    dataEsReingreso = url11.json()
    url12 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoCuenta")
    dataTipoCuenta = url12.json()
    url13 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/DecimoTerceroDecimoCuarto")
    dataDecimoTerceroDecimoCuarto = url13.json()
    url14 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
    dataCentroCostos = url14.json()
    url15 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CategoriaOcupacional")
    dataCategoriaOcupacional = url15.json()
    url16 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/FondoReserva")
    dataFondoReserva = url16.json()
    url17 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/EstadoTrabajador")
    dataEstadoTrabajador = url17.json()

    return render(request, 'agregarTrabajador.html',{
        'id': id,
        'dataSucursal': dataSucursal,
        'dataTipoTrabajador': dataTipoTrabajador,
        'dataGenero': dataGenero,
        'dataOcupaciones': dataOcupaciones,
        'dataCategoriaOcupacional': dataCategoriaOcupacional,
        'datacentroCostos': dataCentroCostos,
        'dataNivelSalarial': dataNivelSalarial,
        'dataTipoContrato': dataTipoContrato,
        'dataTipoCese': dataTipoCese,
        'dataEstadoCivil': dataEstadoCivil,
        'dataTipoComision': dataTipoComision,
        'dataPeriodoVacaciones': dataPeriodoVacaciones,
        'dataEsReingreso': dataEsReingreso,
        'dataTipoCuenta': dataTipoCuenta,
        'dataDecimoTerceroDecimoCuarto': dataDecimoTerceroDecimoCuarto,
        'dataFondoReserva': dataFondoReserva,
        'dataEstadoTrabajador': dataEstadoTrabajador,
    })

def trabajadoresPost(request):
    ##Buscar tipo trabajador 
    url2 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoTrabajador")
    dataTipoTrabajador = url2.json()

    ##Buscar por genero 
    url3 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/Genero")
    dataGenero = url3.json()

    ##Buscar codigo categoria ocupacional
    url15 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CategoriaOcupacional")
    dataCategoriaOcupacional = url15.json()

    ##Buscar codigo de Ocupacion
    url4 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/Ocupaciones")
    dataOcupaciones = url4.json()

    #Buscar codigo periodo de vacaiones
    url10 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/PeriodoVacaciones")
    dataPeriodoVacaciones = url10.json()

    url5 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/NivelSalarial")
    dataNivelSalarial = url5.json()

    ##Buscar codigo de Centro de Costos
    url14 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
    dataCentroCostos = url14.json()

    ##Buscar forma calculo 13
    url13 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/DecimoTerceroDecimoCuarto")
    dataDecimoTerceroDecimoCuarto = url13.json()

    ##Buscar genero el codigo
    url3 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/Genero")
    dataGenero = url3.json()

    ##Buscar Fondo el codigo
    url16 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/FondoReserva")
    dataFondoReserva = url16.json()

    ##Buscar estado del trabajador
    url17 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/EstadoTrabajador")
    dataEstadoTrabajador = url17.json()

    url6 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoContrato")
    dataTipoContrato = url6.json()

    url7 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoCese")
    dataTipoCese = url7.json()

    url8 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/EstadoCivil")
    dataEstadoCivil = url8.json()

    url9 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoComision")
    dataTipoComision = url9.json()

    url11 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/EsReingreso")
    dataEsReingreso = url11.json()

    url12 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoCuenta")
    dataTipoCuenta = url12.json()

    if request.method == "POST":
        COMP_Codigo = request.POST['COMP_Codigo']
        Tipo_trabajador = request.POST['Tipo_trabajador']
        Apellido_Paterno = request.POST['Apellido_Paterno']
        Apellido_Materno = request.POST['Apellido_Materno']
        Nombres = request.POST['Nombres']
        Identificacion = request.POST['Identificacion']
        Entidad_Bancaria = request.POST['Entidad_Bancaria']
        CarnetIESS = request.POST['CarnetIESS']
        Direccion = request.POST['Direccion']
        Telefono_Fijo = request.POST['Telefono_Fijo']
        Telefono_Movil = request.POST['Telefono_Movil']
        Genero = request.POST['Genero']
        Nro_Cuenta_Bancaria = request.POST['Nro_Cuenta_Bancaria']
        Codigo_Categoria_Ocupacion = request.POST['Codigo_Categoria_Ocupacion']
        Ocupacion = request.POST['Ocupacion']
        Centro_Costos = request.POST['Centro_Costos']
        Nivel_Salarial = request.POST['Nivel_Salarial']
        EstadoTrabajador = request.POST['EstadoTrabajador']
        Tipo_Contrato = request.POST['Tipo_Contrato']
        Tipo_Cese = request.POST['Tipo_Cese']
        EstadoCivil = request.POST['EstadoCivil']
        TipodeComision = request.POST['TipodeComision']
        FechaNacimiento = request.POST['FechaNacimiento']
        FechaIngreso = request.POST['FechaIngreso']
        FechaCese = request.POST['FechaCese']
        PeriododeVacaciones = request.POST['PeriododeVacaciones']
        FechaReingreso = request.POST['FechaReingreso']
        Fecha_Ult_Actualizacion = request.POST['Fecha_Ult_Actualizacion']
        EsReingreso = request.POST['EsReingreso']
        Tipo_Cuenta = request.POST['Tipo_Cuenta']
        FormaCalculo13ro = request.POST['FormaCalculo13ro']
        FormaCalculo14to = request.POST['FormaCalculo14to']
        BoniComplementaria = request.POST['BoniComplementaria']
        BoniEspecial = request.POST['BoniEspecial']
        Remuneracion_Minima = request.POST['Remuneracion_Minima']
        Fondo_Reserva = request.POST['Fondo_Reserva']
        Mensaje = request.POST['Mensaje']

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabajadorSelect?sucursal="+COMP_Codigo)
        data = url.json()

        for i in dataTipoTrabajador:
            if i['Codigo'] == Tipo_trabajador:
                Tipo_trabajador = i['Descripcion']

        for i in dataGenero:
            if i['Descripcion'] == Genero:
                Genero = i['Codigo']
        
        for i in dataCategoriaOcupacional:
            if i['Descripcion'] == Codigo_Categoria_Ocupacion:
                Codigo_Categoria_Ocupacion = i['Codigo']

        for i in dataOcupaciones:
            if i['Descripcion'] == Ocupacion:
                Ocupacion = i['Codigo']

        for i in dataNivelSalarial:
            if i['Descripcion'] == Nivel_Salarial:
                Nivel_Salarial = i['Codigo']

        for i in dataPeriodoVacaciones:
            if i['Descripcion'] == PeriododeVacaciones:
                PeriododeVacaciones = i['Codigo']
        
        for i in dataCentroCostos:
            if i['NombreCentroCostos'] == Centro_Costos:
                Centro_Costos = i['Codigo']

        for i in dataDecimoTerceroDecimoCuarto:
            if i['Descripcion'] == FormaCalculo13ro:
                FormaCalculo13ro = i['Codigo']

        ##Buscar forma calculo 14
        for i in dataDecimoTerceroDecimoCuarto:
            if i['Descripcion'] == FormaCalculo14to:
                FormaCalculo14to = i['Codigo']

        for i in dataGenero:
            if i['Descripcion'] == Genero:
                Genero = i['Codigo']
        
        for i in dataFondoReserva:
            if i['Descripcion'] == Fondo_Reserva:
                Fondo_Reserva = i['Codigo']

        for i in dataEstadoTrabajador:
            if i['Descripcion'] == EstadoTrabajador:
                EstadoTrabajador = i['Codigo']

        for i in dataTipoContrato:
            if i['Descripcion'] == Tipo_Contrato:
                Tipo_Contrato = i['Codigo']

        for i in dataTipoCese:
            if i['Descripcion'] == Tipo_Cese:
                Tipo_Cese = i['Codigo']

        for i in dataEstadoCivil:
            if i['Descripcion'] == EstadoCivil:
                EstadoCivil = i['Codigo']

        for i in dataTipoComision:
            if i['Codigo'] == TipodeComision:
                TipodeComision = i['Descripcion']

        for i in dataTipoCuenta:
            if i['Descripcion'] == Tipo_Cuenta:
                Tipo_Cuenta = i['Codigo']

        for i in dataEsReingreso:
            if i['Descripcion'] == EsReingreso:
                EsReingreso = i['Codigo']

        requests.post("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabajadorInsert?COMP_Codigo="+COMP_Codigo+
                      "&Tipo_trabajador="+Tipo_trabajador+"&Apellido_Paterno="+Apellido_Paterno+"&Apellido_Materno="+
                      Apellido_Materno+"&Nombres="+Nombres+"&Identificacion="+Identificacion+"&Entidad_Bancaria="+
                      Entidad_Bancaria+"&CarnetIESS="+CarnetIESS+"&Direccion="+Direccion+"&Telefono_Fijo="+
                      Telefono_Fijo+"&Telefono_Movil="+Telefono_Movil+"&Genero="+Genero+
                      "&Nro_Cuenta_Bancaria="+Nro_Cuenta_Bancaria+"&Codigo_Categoria_Ocupacion="+
                      Codigo_Categoria_Ocupacion+"&Ocupacion="+Ocupacion+"&Centro_Costos="+Centro_Costos+
                      "&Nivel_Salarial="+Nivel_Salarial+"&EstadoTrabajador="+EstadoTrabajador+"&Tipo_Contrato="+Tipo_Contrato+
                      "&Tipo_Cese="+Tipo_Cese+"&EstadoCivil="+EstadoCivil+"&TipodeComision="+TipodeComision+"&FechaNacimiento="+FechaNacimiento+
                      "&FechaIngreso="+FechaIngreso+"&FechaCese="+FechaCese+"&PeriododeVacaciones="+
                      PeriododeVacaciones+"&FechaReingreso="+FechaReingreso+"&Fecha_Ult_Actualizacion="+
                      Fecha_Ult_Actualizacion+"&EsReingreso="+EsReingreso+"&Tipo_Cuenta="+Tipo_Cuenta+
                      "&FormaCalculo13ro="+FormaCalculo13ro+"&FormaCalculo14ro="+FormaCalculo14to+
                      "&BoniComplementaria="+BoniComplementaria+"&BoniEspecial="+BoniEspecial+
                      "&Remuneracion_Minima="+Remuneracion_Minima+"&Fondo_Reserva="+Fondo_Reserva+
                      "&Mensaje="+Mensaje)

        return render(request, 'infoTrabajador.html',{
            'data': data,
            'id': COMP_Codigo,
        })
    
def trabajadoresupdate (request, id, id2):
    if request.method == "POST":
        COMP_Codigo = request.POST['COMP_Codigo']
        Tipo_trabajador = request.POST['Tipo_trabajador']
        Apellido_Paterno = request.POST['Apellido_Paterno']
        Apellido_Materno = request.POST['Apellido_Materno']
        Nombres = request.POST['Nombres']
        Identificacion = request.POST['Identificacion']
        Entidad_Bancaria = request.POST['Entidad_Bancaria']
        CarnetIESS = request.POST['CarnetIESS']
        Direccion = request.POST['Direccion']
        Telefono_Fijo = request.POST['Telefono_Fijo']
        Telefono_Movil = request.POST['Telefono_Movil']
        Genero = request.POST['Genero']
        Nro_Cuenta_Bancaria = request.POST['Nro_Cuenta_Bancaria']
        Codigo_Categoria_Ocupacion = request.POST['Codigo_Categoria_Ocupacion']
        Ocupacion = request.POST['Ocupacion']
        Centro_Costos = request.POST['Centro_Costos']
        Nivel_Salarial = request.POST['Nivel_Salarial']
        EstadoTrabajador = request.POST['EstadoTrabajador']
        Tipo_Contrato = request.POST['Tipo_Contrato']
        Tipo_Cese = request.POST['Tipo_Cese']
        EstadoCivil = request.POST['EstadoCivil']
        TipodeComision = request.POST['TipodeComision']
        FechaNacimiento = request.POST['FechaNacimiento']
        FechaIngreso = request.POST['FechaIngreso']
        FechaCese = request.POST['FechaCese']
        PeriododeVacaciones = request.POST['PeriododeVacaciones']
        FechaReingreso = request.POST['FechaReingreso']
        Fecha_Ult_Actualizacion = request.POST['Fecha_Ult_Actualizacion']
        EsReingreso = request.POST['EsReingreso']
        Tipo_Cuenta = request.POST['Tipo_Cuenta']
        FormaCalculo13ro = request.POST['FormaCalculo13ro']
        FormaCalculo14to = request.POST['FormaCalculo14to']
        BoniComplementaria = request.POST['BoniComplementaria']
        BoniEspecial = request.POST['BoniEspecial']
        Remuneracion_Minima = request.POST['Remuneracion_Minima']
        Fondo_Reserva = request.POST['Fondo_Reserva']
        Mensaje = request.POST['Mensaje']

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabajadorSelect?sucursal="+COMP_Codigo)
        data = url.json()

        ##Buscar codigo categoria ocupacional
        url15 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CategoriaOcupacional")
        dataCategoriaOcupacional = url15.json()

        for i in dataCategoriaOcupacional:
            if i['Descripcion'] == Codigo_Categoria_Ocupacion:
                Codigo_Categoria_Ocupacion = i['Codigo']

        ##Buscar codigo de Ocupacion
        url4 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/Ocupaciones")
        dataOcupaciones = url4.json()

        for i in dataOcupaciones:
            if i['Descripcion'] == Ocupacion:
                Ocupacion = i['Codigo']

        ##Buscar codigo de Centro de Costos
        url14 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
        dataCentroCostos = url14.json()

        for i in dataCentroCostos:
            if i['Descripcion'] == Centro_Costos:
                Centro_Costos = i['Codigo']

        ##Buscar forma calculo 13
        url13 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/DecimoTerceroDecimoCuarto")
        dataDecimoTerceroDecimoCuarto = url13.json()

        for i in dataDecimoTerceroDecimoCuarto:
            if i['Descripcion'] == FormaCalculo13ro:
                FormaCalculo13ro = i['Codigo']

        ##Buscar forma calculo 14
        for i in dataDecimoTerceroDecimoCuarto:
            if i['Descripcion'] == FormaCalculo14to:
                FormaCalculo14to = i['Codigo']
        
        requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabajadorInsert?COMP_Codigo="+COMP_Codigo+
                      "&Tipo_trabajador="+Tipo_trabajador+"&Apellido_Paterno="+Apellido_Paterno+"&Apellido_Materno="+
                      Apellido_Materno+"&Nombres="+Nombres+"&Identificacion="+Identificacion+"&Entidad_Bancaria="+
                      Entidad_Bancaria+"&CarnetIESS="+CarnetIESS+"&Direccion="+Direccion+"&Telefono_Fijo="+
                      Telefono_Fijo+"&Telefono_Movil="+Telefono_Movil+"&Genero="+Genero+
                      "&Nro_Cuenta_Bancaria="+Nro_Cuenta_Bancaria+"&Codigo_Categoria_Ocupacion="+
                      Codigo_Categoria_Ocupacion+"&Ocupacion="+Ocupacion+"&Centro_Costos="+Centro_Costos+
                      "&Nivel_Salarial="+Nivel_Salarial+"&EstadoTrabajador="+EstadoTrabajador+"&Tipo_Contrato="+Tipo_Contrato+
                      "&Tipo_Cese="+Tipo_Cese+"&EstadoCivil="+EstadoCivil+"&TipodeComision="+TipodeComision+"&FechaNacimiento="+FechaNacimiento+
                      "&FechaIngreso="+FechaIngreso+"&FechaCese="+FechaCese+"&PeriododeVacaciones="+
                      PeriododeVacaciones+"&FechaReingreso="+FechaReingreso+"&Fecha_Ult_Actualizacion="+
                      Fecha_Ult_Actualizacion+"&EsReingreso="+EsReingreso+"&Tipo_Cuenta="+Tipo_Cuenta+
                      "&FormaCalculo13ro="+FormaCalculo13ro+"&FormaCalculo14ro="+FormaCalculo14to+
                      "&BoniComplementaria="+BoniComplementaria+"&BoniEspecial="+BoniEspecial+
                      "&Remuneracion_Minima="+Remuneracion_Minima+"&Fondo_Reserva="+Fondo_Reserva+
                      "&Mensaje="+Mensaje)

        return render(request, 'infoTrabajador.html',{
            'data': data,
            'id': id,
        })
    else:        
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabajadorSelect?sucursal="+id)
        data = url.json()
        id2 = int(id2)
        for i in data:
            if i['Id_Trabajador'] == id2:
                data2 = i

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/GetEmisor")
        dataSucursal = url.json()
        url2 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoTrabajador")
        dataTipoTrabajador = url2.json()
        url3 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/Genero")
        dataGenero = url3.json()
        url4 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CategoriaOcupacional")
        dataCategoriaOcupacional = url4.json()
        url5 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/NivelSalarial")
        dataNivelSalarial = url5.json()
        url6 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoContrato")
        dataTipoContrato = url6.json()
        url7 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoCese")
        dataTipoCese = url7.json()
        url8 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/EstadoCivil")
        dataEstadoCivil = url8.json()
        url9 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoComision")
        dataTipoComision = url9.json()
        url10 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/PeriodoVacaciones")
        dataPeriodoVacaciones = url10.json()
        url11 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/EsReingreso")
        dataEsReingreso = url11.json()
        url12 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoCuenta")
        dataTipoCuenta = url12.json()
        url13 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/DecimoTerceroDecimoCuarto")
        dataDecimoTerceroDecimoCuarto = url13.json()
        url14 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
        dataCentroCostos = url14.json()
        url15 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/Ocupaciones")
        dataOcupaciones = url15.json()

        return render(request, 'updateTrabajador.html',{
            'data2': data2,
            'id': id,
            'dataSucursal': dataSucursal,
            'dataTipoTrabajador': dataTipoTrabajador,
            'dataGenero': dataGenero,
            'dataCategoriaOcupacional': dataCategoriaOcupacional,
            'dataNivelSalarial': dataNivelSalarial,
            'dataTipoContrato': dataTipoContrato,
            'dataTipoCese': dataTipoCese,
            'dataEstadoCivil': dataEstadoCivil,
            'dataTipoComision': dataTipoComision,
            'dataPeriodoVacaciones': dataPeriodoVacaciones,
            'dataEsReingreso': dataEsReingreso,
            'dataTipoCuenta': dataTipoCuenta,
            'dataDecimoTerceroDecimoCuarto': dataDecimoTerceroDecimoCuarto,
            'dataOcupaciones': dataOcupaciones,
            'datacentroCostos': dataCentroCostos,
        })

def trabajadoresDelete (request, id, id2):
    id2 = int(id2)
    if request.method == "POST":
        requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabajadorDelete?sucursal="+id+"&codigoempleado=1"+id2)

    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabajadorSelect?sucursal="+id)
    data = url.json()

    return render(request, 'infoTrabajador.html',{
        'data': data,
        'id': id,
    })

def buscartrabajador(request, id):
    if request.method == "POST":
        Codigo = request.POST['Codigo']

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabajadorSelect?sucursal="+id) ##Ir a las sucursales
        data = url.json()
        for i in data: ##Buscar trabajador de las sucursales
            if i['Id_Trabajador'] == int(Codigo):
                data2 = i
        
        return render(request, 'Searchtrabajador.html',{
            'data2': data2,
            'id': id,
        })
        
def pagTipoTrabajador(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoTrabajador")
    data = url.json()

    return render(request, 'tipoTrabajador.html',{
        'data': data,
    })

def pagNivelSalarial(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/NivelSalarial")
    data = url.json()

    return render(request, 'nivelSalarial.html',{
        'data': data,
    })

def pagCategoriaOcupacional(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CategoriaOcupacional")
    data = url.json()

    return render(request, 'categoriaOcupacional.html',{
        'data': data,
    })

def pagTipoCese(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoCese")
    data = url.json()

    return render(request, 'tipoCese.html',{
        'data': data,
    })

def pagTipoContrato(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoContrato")
    data = url.json()

    return render(request, 'tipoContrato.html',{
        'data': data,
    })

def pagEstadoTrabajador(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/EstadoTrabajador")
    data = url.json()

    return render(request, 'estadotrabajador.html',{
        'data': data,
    })