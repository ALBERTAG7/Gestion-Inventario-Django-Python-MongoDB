from django.contrib import admin

from .models import Producto 
admin.site.register(Producto),

from .models import Cliente
admin.site.register(Cliente)

from .models import Empleado
admin.site.register(Empleado)

from .models import Venta
admin.site.register(Venta)

from .models import Proveedor
admin.site.register(Proveedor)

from .models import Inventario
admin.site.register(Inventario)


