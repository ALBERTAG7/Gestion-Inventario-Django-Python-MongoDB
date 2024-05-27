from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from django.contrib.auth import logout
from datetime import datetime
from django.shortcuts import redirect

#base
from .models import Producto
from .models import Cliente
from .models import Empleado
from .models import Venta
from .models import Proveedor
from .models import Inventario

#formularios
from .forms import ProductoForm 
from .forms import ClienteForm
from .forms import EmpleadoForm
from .forms import VentaForm
from .forms import ProveedorForm
from .forms import InventarioForm
from .forms import ProductoForm





#htmls
def nosotros(request):
    return render(request, 'nosotros.html')
@login_required
def inicio(request):
    return render(request, 'inicio.html')


def ubicacion(request):
    return render(request, 'ubicacion.html')

@login_required
def autor(request):
    return render(request, 'autor.html')

#htmls con base
@login_required
def index(request):
    producto= Producto.objects.all() 
    return render(request, 'index.html', {'producto': producto})
    


def Productos(request):
    producto=Producto.objects.all() 
    return render(request, 'producto.html', {'Producto':Producto})

@login_required
def listas_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

@login_required
def Empleados(request):
    empleado= Empleado.objects.all() 
    return render(request, 'empleado.html', {'Empleado':Empleado})


#def Ventas(request):
 #   venta= Venta.objects.all() 
  #  return render(request, 'venta.html', {'Venta':Venta})
@login_required
def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'venta.html', {'ventas': ventas})

@login_required
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedor.html', {'proveedores': proveedores})

@login_required
def Inventarios(request):
    inventario= Inventario.objects.all() 
    return render(request, 'inventario.html', {'Inventario':Inventario})





#Formularios
@login_required
def CrearProducto(request):
    formulario = ProductoForm (request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('crearproducto')
    return render (request, 'crearproducto.html', {'formulario':formulario})
@login_required
def CrearCliente(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('crear_cliente')
    return render (request, 'crear_cliente.html', {'formulario':formulario})
@login_required
def CrearEmpleado(request):
    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('crear_empleado')
    else:
        formulario = EmpleadoForm()
    return render(request, 'crear_empleado.html', {'formulario': formulario})
    

@login_required
def CrearVenta(request):
    if request.method == 'POST':
        formulario = VentaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('crear_venta')
    else:
        formulario = VentaForm()
    return render(request, 'crear_venta.html', {'formulario': formulario})

@login_required
def CrearProveedor(request):
    formulario = ProveedorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('crear_proveedor')
    return render (request, 'crear_proveedor.html', {'formulario':formulario})
@login_required
def CrearInventario(request):
    formulario = InventarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('CrearInventario')
    return render (request, 'crearinventario.html', {'formulario':formulario})

@login_required
def eliminar(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto) 
    producto.delete()
    return redirect('index')
@login_required
def EliminarCliente(request, clave_cliente):
    cliente = Cliente.objects.get(clave_cliente=clave_cliente) 
    cliente.delete()
    return redirect('EliminarCliente')
@login_required
def EliminarEmpleado(request, clave_empleado):
    empleado = Empleado.objects.get(clave_empleado=clave_empleado) 
    empleado.delete()
    return redirect('EliminarEmpleado')

@login_required
def EliminarVenta(request, folio_venta):
    venta=Venta.objects.get(folio_venta=folio_venta) 
    venta.delete()
    return redirect('EliminarVenta')

@login_required
def EliminarProveedor (request,clave_proveedor):
    proveedor= Proveedor.objects.get(clave_proveedor=clave_proveedor) 
    proveedor.delete()
    return redirect('EliminarProveedor')

#maquinaria
def EliminarInventario (request,clave_PInventario):
    inventario= Inventario.objects.get(clave_PInventario=clave_PInventario) 
    inventario.delete()
    return redirect('EliminarInventario')


#Ventas

@login_required
def busqueda(request):
    query = request.GET.get('query')

    if query:
        # Intenta analizar la cadena de consulta como una fecha en formato 'YYYY-MM-DD'
        try:
            fecha_consulta = datetime.strptime(query, '%Y-%m-%d')
            resultados = Venta.objects.filter(fecha=fecha_consulta)
        except ValueError:
            # Si la cadena no se puede analizar como fecha, busca por otros campos
            resultados = Venta.objects.filter(clave_empleado__icontains=query) | \
                         Venta.objects.filter(nombre_cliente__icontains=query)
    else:
        # Si no hay consulta, muestra la lista completa
        resultados = []

    return render(request, 'bventas.html', {'resultados': resultados})






def lista_productos(request):
 
    productos = Producto.objects.all()
 
    return render(request, 'lista_productos.html', {'productos': productos})

def eliminar_producto(request, producto_id):
    # Lógica para eliminar el producto
    return redirect('lista_productos')

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crearproducto')
    else:
        form = ProductoForm()
    
    return render(request, 'crearproducto.html', {'formulario': form})

def exit(request):
    logout(request)
    return redirect('login')

@login_required
def editar_productos(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('guardar_'):
                producto_id = key.split('_')[1]
                nombre = request.POST.get('nombre_' + producto_id)
                marca = request.POST.get('marca_' + producto_id)
                precio = request.POST.get('precio_' + producto_id)

                # Obtener el objeto Producto a editar
                producto = Producto.objects.get(id_producto=producto_id)

                # Actualizar los campos del producto
                producto.nombre = nombre
                producto.marca = marca
                producto.precio = precio

                # Guardar los cambios en la base de datos
                producto.save()

            elif key.startswith('eliminar_'):
                producto_id = key.split('_')[1]
                Producto.objects.filter(id_producto=producto_id).delete()

        return redirect('editar_productos')

    else:
        productos = Producto.objects.all()
        return render(request, 'editar_productos.html', {'productos': productos})
    
@login_required 
def crear(request):
    # Lógica para crear algo aquí
    return render(request, 'crear.html')
    
