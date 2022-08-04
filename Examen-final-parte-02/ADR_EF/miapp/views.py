from django.shortcuts import render, HttpResponse
from miapp.models import Producto
from miapp.models import Curso
# Create your views here.


def inicio(request):
    mensaje = '¡Hola! Este es el Examen Final'
    return render(request, 'inicio.html', {'mensaje': mensaje})


def integrantes(request):
    integrantes = [ 'Rodriguez Mejia Jose Jean Piere',
                    'Azañero Espinoza Waldir',
                    'Diaz Seminario Daniel', ]
    return render(request,'integrantes.html',{'integrantes':integrantes})


def crear_productos(request):
    producto = Producto(
	codigo = "06",
	nombre = "plumones",
	precio_compra = "5.00",
	precio_venta = "7.00",
    fecha_compra = "31/07/2022",
	estado = "A",
	)
    producto.save()
    return render(request, 'crear-productos.html',
        {'producto' : producto})


def crear_cursos(request):
    curso = Curso(
	codigo = "08",
	nombre = "hacking",
	horas = "8.00",
	creditos = "6.00",
	estado = "A",
	)
    curso.save()
    return render(request, 'crear-cursos.html',
        {'curso' : curso})