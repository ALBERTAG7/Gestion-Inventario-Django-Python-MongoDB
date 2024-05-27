from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    marca = models.CharField(max_length=100, verbose_name='producto')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    precio= models.DecimalField(max_digits=10, decimal_places=2,verbose_name='precio')

class Cliente(models.Model):
    clave_cliente= models.AutoField(primary_key=True)
    nombre_cliente=models.CharField(max_length=100, verbose_name='nombre')
    telefono= models.BigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000000000000)], verbose_name='telefono')

class Empleado(models.Model):
    clave_empleado= models.AutoField(primary_key=True)
    nombre_empleado=models.CharField(max_length=100, verbose_name='nombre')
    telefono= models.BigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000000000000)], verbose_name='telefono')
    salario= models.DecimalField(max_digits=10, decimal_places=2, verbose_name='salario')
    horario= models.CharField(max_length=100, verbose_name='horario')
    numero_de_seguro= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000000000000)],verbose_name='numero_de_seguro')
    
class Venta(models.Model):
    folio_venta = models.AutoField(primary_key=True)
    clave_empleado  = models.CharField(max_length=100, verbose_name='Clave del empleado')
    nombre_cliente = models.CharField(max_length=100, verbose_name='Nombre del cliente')
    fecha = models.DateField(verbose_name='Fecha de venta')
    producto = models.CharField(max_length=100, verbose_name='Producto')
    precio= models.DecimalField(max_digits=10, decimal_places=2,verbose_name='precio')

class Proveedor(models.Model):
    clave_proveedor= models.AutoField(primary_key=True)
    nombre_producto= models.CharField(max_length=100, verbose_name='Nombre Producto')
    marca_producto= models.CharField(max_length=100, verbose_name='Marca Producto')
    precio_producto= models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Precio Producto')
    cantidad_producto= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000000000000)],verbose_name='Cantidad Producto')
    fecha_entrada= models.DateField(verbose_name='Fecha de entrada')
    fecha_salida= models.DateField(verbose_name='Fecha de salida')
    telefono= models.BigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000000000000)],verbose_name='Telefono')
   
class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField(null=True, blank=True)