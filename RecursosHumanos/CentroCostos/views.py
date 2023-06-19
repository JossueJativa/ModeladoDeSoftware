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
                'message': "Ingreso mal un campo"
            })

        if data[0]['OBSERVACION'] == "INGRESO EXITOSO":
            return render(request, 'exception.html',{
                'message': "Ingreso Exitoso"
            })
    else:
        return render(request, 'login.html')
    
