from django.shortcuts import render, redirect, get_object_or_404
from .models import Flora
from .forms import FloraForm

# Create your views here.

def index(request):
    return render(request, 'flora/index.html')

def donaciones(request):
    return render(request, 'flora/donaciones.html')

def usuario(request):
    return render(request, 'flora/usuario.html')

def tienda(request):
    floras = Flora.objects.all()
    data = {
        'floras': floras
    }
    return render(request, 'flora/tienda.html', data)

def inicio(request):
    return render(request, 'flora/index.html')

def agregar_flora(request):
    
    data = {
        'form': FloraForm()
    }
    
    if request.method == 'POST':
        formulary = FloraForm(data=request.POST,files=request.FILES)
        if formulary.is_valid():
            formulary.save()
            return redirect(to="listar_floras")
        else:
            data ['form'] = formulary
    
    return render(request, 'flora/floras/agregar.html', data)

def listar_floras(request):
    floras = Flora.objects.all()
    data = {
        'floras': floras
    }
    return render(request, 'flora/floras/listar.html', data)

def modificar_floras(request,id):
    
    flora = get_object_or_404(Flora,id = id)
    data = {
        'form': FloraForm(instance = flora)   
    }
    if request.method == 'POST':
            formulary = FloraForm(data=request.POST,instance=flora,files=request.FILES)
            if formulary.is_valid():
                formulary.save()
                return redirect(to="listar_floras")
            data ['form'] = formulary
    return render(request, 'flora/floras/modificar.html', data)

def eliminar_floras(request,id):
    flora = get_object_or_404(Flora,id = id)
    flora.delete()
    return redirect(to="listar_floras")
    





