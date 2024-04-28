from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app_crm/home.html')

def produtos(request):
    return render(request, 'app_crm/produtos.html')

def clientes(request):
    return render(request, 'app_crm/clientes.html')