from django.shortcuts import render

def index(request):
    return render(request, 'servicios/index.html')

def modelos_servicio(request):
    return render(request, 'servicios/modelos_servicio.html')

def saas(request):
    return render(request, 'servicios/saas.html')

def paas(request):
    return render(request, 'servicios/paas.html')

def iaas(request):
    return render(request, 'servicios/iaas.html')