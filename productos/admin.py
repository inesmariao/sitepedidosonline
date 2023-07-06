from django.contrib import admin
# from productos.models import Categoria, Marca, Color, Medida, Producto, Imagen, Presentacion
from .models import *

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Color)
admin.site.register(Medida)


class ImagenInline(admin.TabularInline):
    model = Imagen
    

class PresentacionInline(admin.StackedInline):
    model = Presentacion


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "codigo", "categoria", "marca", "precio"]
    search_fields = ["titulo", "codigo", "categoria__nombre", "marca__nombre"]
    list_filter = ["marca", "categoria"]
    # clase de TabularInline o StackedInline
    inlines = [ImagenInline, PresentacionInline]


admin.site.register(Producto, ProductoAdmin)






class ImagenAdmin(admin.ModelAdmin):
    list_display = ["producto", "orden", "nombre"]

admin.site.register(Imagen, ImagenAdmin)

class PresentacionAdmin(admin.ModelAdmin):
    list_display = ["producto", "stock", "medida", "color"]

admin.site.register(Presentacion, PresentacionAdmin)