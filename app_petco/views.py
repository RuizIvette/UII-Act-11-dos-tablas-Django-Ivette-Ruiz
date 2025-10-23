from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Mascota
from .forms import ClienteForm, MascotaForm

# Create your views here.
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'listar_mascotas.html', {'mascotas': mascotas})

def detalle_mascota(request, id_mascota):
    mascota = get_object_or_404(Mascota, id_mascota=id_mascota)
    return render(request, 'detalle_mascota.html', {'mascota': mascota})

def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_petco:listar_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'formulario_mascota.html', {'form': form, 'titulo': 'Registrar Nueva Mascota'})

def editar_mascota(request, id_mascota):
    mascota = get_object_or_404(Mascota, id_mascota=id_mascota)
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('app_petco:detalle_mascota', id_mascota=mascota.id_mascota)
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'formulario_mascota.html', {'form': form, 'titulo': 'Editar Mascota'})

def borrar_mascota(request, id_mascota):
    mascota = get_object_or_404(Mascota, id_mascota=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('app_petco:listar_mascotas')
    return render(request, 'confirmar_borrar_mascota.html', {'mascota': mascota})

# --- Vistas para Clientes ---

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def detalle_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    return render(request, 'detalle_cliente.html', {'cliente': cliente})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_petco:listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'formulario_cliente.html', {'form': form, 'titulo': 'Registrar Nuevo Cliente'})

def editar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('app_petco:detalle_cliente', id_cliente=cliente.id_cliente)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'formulario_cliente.html', {'form': form, 'titulo': 'Editar Cliente'})

def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('app_petco:listar_clientes')
    return render(request, 'confirmar_borrar_cliente.html', {'cliente': cliente})