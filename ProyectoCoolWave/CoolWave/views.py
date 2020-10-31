from django.shortcuts import render
from .models import SliderIndex,MisionVision, Insumos


from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout, login as login_aut
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.
def index(request):
    autos = SliderIndex.objects.all()
    return render(request,'web/index.html',{'autos':autos})

def reserva(request):
    return render(request,'web/reserva.html')

def galeria(request):
    return render(request,'web/galeria_imagenes.html')

def quienes(request):
    mv= MisionVision.objects.all()
    return render(request,'web/quienes_somos.html',{'mv':mv})

def local(request):
    return render(request,'web/locales.html')

def registro(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtCorreo")
        pass1 = request.POST.get("txtPass1")
        pass2 = request.POST.get("txtPass2")
        usuario = request.POST.get("txtUsuario")

        if pass1!=pass2:
            return render(request,'web/formulario_registro.html',{'msg':'contrasenias incorrectas'})

        try:
            usu = User.objects.get(username=usuario)
            return render(request,'web/formulario_registro.html',{'msg':'usuario existente'})
        except:
            usu = User()
            usu.first_name = nombre
            usu.last_name = apellido
            usu.email = email
            usu.set_password(pass1)
            usu.username = usuario
            usu.save()

            us = authenticate(request, username=usuario, password=pass1)
            login_aut(request,us)

            autos = SliderIndex.objects.all()
            return render(request,'web/index.html',{'autos':autos})

    return render(request,'web/formulario_registro.html')

def login(request):
    if request.POST:
        usuario = request.POST.get("txtNombreP")
        password = request.POST.get("txtPass")
        us = authenticate(request, username=usuario, password=password)
        if us is not None and us.is_active:
            login_aut(request,us)
            autos = SliderIndex.objects.all()
            return render(request,'web/index.html',{'autos':autos}) 
        else:
            return render(request,'web/login.html',{'msg':'no existe'})
    return render(request,'web/login.html')

def cerrar_sesion(request):
    logout(request)
    autos = SliderIndex.objects.all()
    return render(request,'web/index.html',{'autos':autos})

@login_required(login_url='/inicio_sesion/')
@permission_required('CoolWave.view_insumos',login_url='/inicio_sesion/')
@permission_required('CoolWave.change_insumos',login_url='/inicio_sesion/')
def modificar(request):
    msg=''
    if request.POST:
        nombre = request.POST.get("txtNombreP")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")
        stock = request.POST.get("txtStock")

        try:
            insumo = Insumos.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = descripcion
            insumo.stock = stock
            insumo.save()
            msg='Modifico'
        except:
            msg='No Modifico'

    insumos = Insumos.objects.all()
    return render(request,'web/admin_productos.html',{'lista_insumos':insumos,'msg':msg})



@login_required(login_url='/inicio_sesion/')
@permission_required('CoolWave.view_insumos',login_url='/inicio_sesion/')
def busqueda_mod(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        return render(request,'web/productos_mod.html',{'insumo':insumo})
    except:
        msg='Mo Ubico el insumo'
    insumos = Insumos.objects.all()
    return render(request,'web/admin_productos.html',{'lista_insumos':insumos,'msg':msg})

@login_required(login_url='/inicio_sesion/')
@permission_required('CoolWave.delete_insumos',login_url='/inicio_sesion/')
def eliminar(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg='Elimino Insumo'
    except:
        msg='Mo Elimino Insumo'
    insumos = Insumos.objects.all()
    return render(request,'web/admin_productos.html',{'lista_insumos':insumos,'msg':msg})

@login_required(login_url='/inicio_sesion/')
@permission_required('CoolWave.view_insumos',login_url='/inicio_sesion/')
def lista_insumos(request):
    insumos = Insumos.objects.all()
    return render(request,'web/admin_productos.html',{'lista_insumos':insumos})

@login_required(login_url='/inicio_sesion/')
@permission_required('CoolWave.add_insumos',login_url='/inicio_sesion/')
def producto(request):
    if request.POST:
        nombre = request.POST.get("txtNombreP")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")
        stock = request.POST.get("txtStock")
        insumo = Insumos(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock
        )
        insumo.save()
        return render(request,'web/productos.html',{'msg':'grabo insumo'})
    return render(request,'web/productos.html')
