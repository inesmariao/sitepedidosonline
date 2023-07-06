from django.contrib import admin
from pedidos.models import Cliente, Pedido, DetallePedido


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'email', 'dni', 'celular', 'direccion', 'usuario']
    fieldsets = (
        # datos personales
        ("Datos personales", {
            "fields": (
                ("apellidos", "nombres", "dni"), 
            )
        }),
        # datos de contacto
        ("Datos de contacto", {
            "fields": (
                ('email', 'celular', 'direccion')
            )
        }
        ),
        # datos de usuario
        ("Datos de usuario", {
            "fields": (
                "usuario",
            )
        }),
    )
    search_fields = ["nombres", "apellidos", "dni"]

admin.site.register(Cliente, ClienteAdmin)


class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido


class PedidoAdmin(admin.ModelAdmin):
    list_display = ["fecha", "numero", "formato_total", "cliente"]
    search_fields = ["fecha", "numero", "cliente__nombres"]
    # list_filter = ["cliente", "fecha"]
    inlines = [DetallePedidoInline]
    # autocomplete_fields = ["cliente"]
    raw_id_fields = ["cliente"]

    
admin.site.register(Pedido, PedidoAdmin)

    
admin.site.register(DetallePedido)