from django.shortcuts import render

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
    
