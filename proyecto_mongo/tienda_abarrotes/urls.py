from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from .views import lista_productos

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('nosotro/', views.nosotros),  # Redirección
    path('inicio/', views.inicio, name='inicio'),
    path('inicio/', views.inicio),  # Redirección
    path('login/', views.inicio),  # Redirección
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('autor/', views.autor, name='autor'),
    path('index/', views.index, name='index'),
    path('producto/', views.Productos, name='producto'),
    path('produc/', views.Productos),  # Redirección
    path('lista_clientes/', views.listas_cliente, name='lista_clientes'),
    path('empleado/', views.Empleados, name='empleado'),
    path('venta/', views.lista_ventas, name='venta'),
    path('lista_proveedor/', views.lista_proveedores, name='lista_proveedor'),
    path('inventario/', views.Inventarios, name='inventario'),
    path('crearproducto/', views.CrearProducto, name='crearproducto'),
    path('crear_cliente/', views.CrearCliente, name='crear_cliente'),
    path('cliente_nuevo/', views.CrearCliente),  # Redirección
    path('crear_proveedor/', views.CrearProveedor, name='crear_proveedor'),
    path('editar_productos/', views.editar_productos, name='editar_productos'),
    path('eliminar/<int:id_producto>/', views.eliminar, name='eliminar'),
    path('eliminarcliente/<int:clave_cliente>/', views.EliminarCliente, name='eliminarcliente'),
    path('eliminar_empleado/<int:clave_empleado>/', views.EliminarEmpleado, name='eliminarempleado'),
    path('eliminarventa/<int:folio_venta>/', views.EliminarVenta, name='eliminarventa'),
    path('eliminarproveedor/<int:clave_proveedor>/', views.EliminarProveedor, name='eliminarproveedor'),
    path('eliminarinventario/<int:clave_PInventario>/', views.EliminarInventario, name='eliminarinventario'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('buscar/', views.busqueda),  # Redirección
    path('buscar/ventas/', views.busqueda, name='bventas'),
    path('bventas/', views.busqueda, name='bventas'),
    path('lista_productos/', lista_productos, name='lista_productos'),
    path('lista_productos/autor/', views.autor, name='autor'),
    path('eliminar_producto/', views.eliminar_producto),  # Sin ID
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('producto/<categoria>/', views.Productos),  # Por categoría
    path('venta/<int:id>/detalle/', views.lista_ventas),  # Detalles de venta
    path('crearproducto/', views.CrearProducto),  # Corrección del nombre
    path('crear_empleado/', views.CrearEmpleado, name='crear_empleado'),
    path('crear_venta/', views.CrearVenta, name='crear_venta'),
    path('logout/', views.exit, name='exit'),
     # Redirección
    # Rutas adicionales para manejar casos no encontrados
    path('producto/<int:id>/editar/', views.CrearProducto),  # Redirigir a crear_producto
    path('lista_productos/bventas/', views.busqueda),  # Redirigir a búsqueda de ventas
    path('crear/', views.crear_producto),
     path('crear/', views.crear, name='crear'),
     # Redirigir a crear_producto
    path('ventas/', views.lista_ventas),  # Redirigir a lista de ventas
    path('lista_proveedor/', views.lista_proveedores),  # Redirigir a lista de proveedores
    path('inventario/<int:id>/', views.Inventarios),  # Redirigir a detalles de inventario
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

