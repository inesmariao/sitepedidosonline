from django.shortcuts import render
from django.http import HttpResponse

def listado_usuarios(request):
    # logica, algoritmos, conectar a la BD, conectar a una API, enviar un correo
    # 
    print(request.GET)
    nombre = request.GET.get("nombre", "-")
    apellido = request.GET.get("apellido", "+")
    # apellido
    return HttpResponse("Listado de usuarios: " + nombre + "" + apellido)


def crear_usuario(request):
    # retornar el contenido de un TEMPLATE -> archivo html
    return render(request, "formulario.html", {})


def editar_usuario(request, id, tipo):
    return HttpResponse("El id del usuario es:" + str(tipo))