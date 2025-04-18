from django.db import models

# Create your models here.
class Descuentos(models.Model):
    id_producto=models.ForeignKey('Productos', on_delete=models.CASCADE, db_column='id_producto')
    porcentaje = models.IntegerField()
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'descuentos'

class Devoluciones(models.Model):
    id_producto = models.ForeignKey('Productos', on_delete=models.CASCADE, db_column='id_producto')
    motivo = models.CharField(max_length=300)
    correo = models.CharField(max_length=50)
    fecha_compra = models.DateField()
    fecha_devolucion = models.DateField()

    class Meta:
        managed = False
        db_table = 'devoluciones'

class Inventario(models.Model):
    id_producto = models.ForeignKey('Productos', on_delete=models.CASCADE, db_column='id_producto')
    id_sucursal = models.ForeignKey('Sucursales', on_delete=models.CASCADE, db_column='id_sucursal')
    cantidad = models.IntegerField()
    fecha_entrada = models.DateField()
    fecha_caducidad = models.DateField()
    fecha_restock = models.DateField()

    class Meta:
        managed = False
        db_table = 'inventario'

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        #managed = False
        db_table = 'productos'
        verbose_name = "Producto"

class Roles(models.Model):
    rol = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'roles'

class Sucursales(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sucursales'

class Usuarios(models.Model):
    user = models.CharField(max_length=20)
    contrasenia = models.CharField(max_length=25)
    id_rol = models.ForeignKey(Roles, on_delete=models.CASCADE, db_column='id_rol')

    class Meta:
        managed = False
        db_table = 'usuarios'