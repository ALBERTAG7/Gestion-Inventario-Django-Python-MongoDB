from django import forms
from .models import Producto
from .models import Cliente
from .models import Empleado
from .models import Venta
from .models import Proveedor
from .models import Inventario


class ProductoForm (forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__' 

class EmpleadoForm (forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'      

class VentaForm (forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'


class ProveedorForm (forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'


class InventarioForm (forms.ModelForm):
    class Meta:
        model = Inventario
        fields = '__all__'

