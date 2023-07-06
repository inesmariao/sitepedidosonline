from django.db import models
from django.contrib.auth.models import User
from productos.models import Presentacion
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib import admin
from django.utils.html import format_html


def validar_dni(value):
    # None y Null
    if value is not None and value != '':
        if len(value) < 8:
            raise ValidationError("El DNI debe tener al menos 8 caracteres")
        elif len(value) > 10:
            raise ValidationError("El DNI debe tener al maximo 10 caracteres")


class Cliente(models.Model):
    nombres = models.CharField("Nombres", max_length=100)
    apellidos = models.CharField("Apellidos", max_length=100)
    email = models.EmailField("Email", max_length=70)
    direccion = models.CharField(
        "Dirección", max_length=45, null=True, blank=True)
    celular = models.CharField("Celular", max_length=20, null=True, blank=True)
    dni = models.CharField("DNI", max_length=20, null=True,
                           blank=True, validators=[validar_dni])
    usuario = models.OneToOneField(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

    class Meta:
        db_table = "cliente"


class Pedido(models.Model):
    # fecha = models.DateField(auto_now_add=True)
    fecha = models.DateField(default=timezone.now)
    numero = models.CharField("Número", max_length=10, editable=False)
    total = models.DecimalField("Total", max_digits=9, decimal_places=2, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    
    @admin.display
    def formato_total(self):
        if self.total > 100:
            return format_html("<strong style='color:green'>$ " + str(self.total) + "</strong>")
        else:
            return format_html("<strong style='color:red'>$ " + str(self.total) + "</strong>")

    def __str__(self):
        return self.numero
    
    
    # sobre el metodo save()
    def save(self):
        # save: se usa cuando se crea un nuevo registro o se actualiza
        if self.id is None:
            self.total = 0.00
            self.numero = "0000000"
        return super().save()

    class Meta:
        db_table = "pedido"


class DetallePedido(models.Model):
    cantidad = models.IntegerField(default=0)
    precio_unitario = models.DecimalField(
        "Precio Unitario", max_digits=9, decimal_places=2)
    pedido = models.ForeignKey(Pedido, on_delete=models.RESTRICT)
    presentacion = models.ForeignKey(
        Presentacion, on_delete=models.RESTRICT, verbose_name="Presentación")

    def __str__(self):
        return self.pedido.numero
    
    
    # sobre escribir el metodo SAVE()
    def save(self):
        # el pedido ya esta en la BD
        if self.id is None:
            pedido_padre = self.pedido
            total = pedido_padre.total # 500.00
            total = total + float(self.cantidad * self.precio_unitario)
            pedido_padre.total = total
            pedido_padre.save() # actualizando el total del mi pedida
        
        # se ejecutar el metodo save() de la clase padre
        return super().save()

    class Meta:
        db_table = "detalle_pedido"
