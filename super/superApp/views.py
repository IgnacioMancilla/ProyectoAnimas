from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from superApp.models import *
from django.core.exceptions import * 


from django.shortcuts import redirect
# Create your views here.


def main(request):
    titulo = "Supermercado Las Ánimas"
    data = {'titulo':titulo}
    return render(request,'templatesApp/main.html',data)


def categoria(request):
    titulo = "Categorías"
    data = {'titulo':titulo}
    return render(request,'templatesApp/categoria.html',data)


def gestion(request):
    titulo = "Gestión"
    contador =0
    productos = Producto.objects.all()
    for i in productos:
        contador +=1
    data = {'producto':productos,'contador':contador,'titulo':titulo}
    if request.method == "POST":
        nombre = request.POST.get("productoName") 
        categoria = request.POST.get("categoria")
        stock = request.POST.get("productoStock")
        precio= request.POST.get("productoPrice")
        imagen = request.FILES.get('imagen')

        producto = Producto()
        producto.nombre = nombre
        producto.categoria = categoria.capitalize()
        producto.stock = stock
        producto.precio = precio
        producto.imagen = imagen
        Producto.save(producto)
        return redirect("/gestion/")
    return render(request,'templatesApp/gestion.html',data)


def contacto(request):
    titulo = "Formulario contacto"
    data = {'titulo':titulo}
    if request.method == "POST":
         
         tipo_consulta = request.POST.get("tipo_consulta")
         correo = request.POST.get("correo")
         imagen = request.FILES.get("imagen")
         telefono = request.POST.get("telefono")
         descripcion = request.POST.get("descripcion")
         estado = "Pendiente"
         formulario = Formulario()
         
         formulario.tipo_consulta = tipo_consulta
         formulario.correo_electronico = correo
         formulario.imagen = imagen
         formulario.telefono = telefono
         formulario.descripcion = descripcion
         formulario.estado = estado
         Formulario.save(formulario)
         return redirect('/agradecimiento/')
    
    return render(request,'templatesApp/contacto.html',data)

def producto(request,categoria):
    
    if categoria.capitalize() == "Lacteos":
            producto = Producto.objects.filter(categoria = "Lacteos")
            titulo = "Lácteos"
            data = {'producto':producto,'titulo':titulo}
            
    elif categoria.capitalize() == "Carnes":
            producto = Producto.objects.filter(categoria = "Carnes")
            titulo = "Carnes"
            data = {'producto':producto,'titulo':titulo}

    elif categoria.capitalize() == "Herramientas":
            producto = Producto.objects.filter(categoria = "Herramientas")
            titulo = "Herramientas"
            data = {'producto':producto,'titulo':titulo}

    elif categoria.capitalize() == "Cuidado":
            producto = Producto.objects.filter(categoria = "Cuidado personal")
            titulo = "Cuidado"
            data = {'producto':producto,'titulo':titulo}

    elif categoria.capitalize() == "Frutas":
            producto = Producto.objects.filter(categoria = "Frutas y verduras")
            titulo = "Frutas y verduras"
            data = {'producto':producto,'titulo':titulo}

    elif categoria.capitalize() == "Mascotas":
            producto = Producto.objects.filter(categoria = "Mascotas")
            titulo = "Mascotas"
            data = {'producto':producto,'titulo':titulo}

    elif categoria.capitalize() == "Envasados":
            producto = Producto.objects.filter(categoria = "Envasados")
            titulo = "Envasados"
            data = {'producto':producto,'titulo':titulo}  

    elif categoria.capitalize() == "Despensa":
            producto = Producto.objects.filter(categoria = "Despensa")
            titulo = "Despensa"
            data = {'producto':producto,'titulo':titulo}

    return render(request,'templatesApp/productos.html',data)

def editar_producto(request,id):
    productos = Producto.objects.get(id=id)
    
    titulo = "Editar producto"
    data = {'producto':productos,'titulo':titulo}
    if request.method == "POST":
        nombre = request.POST.get("productoName") 
        categoria = request.POST.get("categoria")
        stock = request.POST.get("productoStock")
        precio = request.POST.get("productoPrice")
        imagen = request.FILES.get('imagen')
        imagen_original = productos.imagen

        productos.nombre = nombre
        productos.categoria = categoria.capitalize()
        productos.stock = stock
        productos.precio = precio


        if imagen is not None:
             productos.imagen.delete()
             productos.imagen = imagen
        else:
             productos.imagen = imagen_original
        productos.save()
        return redirect ('/gestion/')
    return render(request,'templatesApp/editar_producto.html',data)

def eliminar_producto(request,id):
    producto = Producto.objects.get(id=id)
    producto.imagen.delete()
    producto.delete()
    return redirect('/gestion/')

def login_user (request):
    titulo = "Inicio de sesión"
    data = {'titulo':titulo}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,"templatesApp/invalido.html",data)

    return render(request,'templatesApp/login.html',data    )

def logout_user(request):
    logout(request)
    return redirect("/")

def perfil(request,id):
     titulo = "Mi cuenta"
     data = {'titulo':titulo}
     if request.method == "POST":
          usuario = User.objects.get(id=id)
          contraseña = request.POST.get('contraseña')
          re_contraseña = request.POST.get('re_contraseña')

          if contraseña == re_contraseña:
               usuario.set_password(contraseña)
               usuario.save()
               logout(request)
               return redirect('/')
            
          else:
               return render(request,'templatesApp/aviso.html',data)
            
     return render(request,'templatesApp/perfil.html',data)

def agradecimiento(request):
     titulo = "Agradecimientos"
     data = {'titulo':titulo}
     return render(request,'templatesApp/agradecimiento.html',data)

def vista_formulario(request):
     titulo = 'Formularios'
     formulario = Formulario.objects.all()
     data = {'data':formulario,'titulo':titulo} 
     return render(request,'templatesApp/vista_formulario.html',data)

def detalles(request,id):
     titulo = "Detalles"
     formulario = Formulario.objects.get(id=id)
     data = {'data':formulario,'titulo':titulo}
     return render(request,'templatesApp/detalles.html',data)

def eliminar_formulario(request,id):
     formulario = Formulario.objects.get(id=id)
     formulario.imagen.delete()
     formulario.delete()
     return redirect('/formularios/')


def aprobar(request,id):
     formulario = Formulario.objects.get(id=id)
     formulario.estado = "Resuelta"
     formulario.save()
     return redirect('/formularios/')

def crear_usuario(request):
     titulo = "Crear usuario"
     data = {'titulo':titulo}
     if request.method == "POST":

          username = request.POST.get('username')
          nombre = request.POST.get('nombre')
          apellido = request.POST.get('apellido')
          correo = request.POST.get('correo')
          tipo_cuenta = request.POST.get('tipo_cuenta')

          
          bandera = True
          usuarios = User.objects.all()
          for i in usuarios:
               if i.username.lower() == username.lower():
                    bandera = False
          if bandera == False:
               return render(request,'templatesApp/usuario_repetido.html',data)
          else:
               user = User.objects.create_user(username)
               user.username = username
               user.first_name = nombre
               user.last_name = apellido
               user.email = correo
               user.set_password(username)
               if tipo_cuenta == "administrador":
                    user.is_superuser = True
               else:
                    user.is_superuser = False
               user.save()
               return redirect('/lista_usuarios/')
     return render(request,'templatesApp/crear_usuario.html',data)


def lista_usuarios(request):
     titulo = "Lista usuarios"
     user = User.objects.all()
     data = {'data':user,'titulo':titulo}
     return render(request,'templatesApp/lista_usuarios.html',data)

def eliminar_usuario(request,id):
     user = User.objects.get(id=id)
     if user.username == "admin":
          return redirect('/lista_usuarios/')
     else:
          user.delete()
          return redirect('/lista_usuarios/')
     
def cambiar_admin(request,id):
     user = User.objects.get(id=id)
     user.is_superuser = True
     user.save()
     return redirect('/lista_usuarios/')

def cambiar_estandar(request,id):
     user = User.objects.get(id=id)
     user.is_superuser = False
     user.save()
     return redirect('/lista_usuarios/')

def restablecer_contraseña(request,id):
     user = User.objects.get(id=id)
     user.set_password(user.username)
     user.save()
     return redirect('/lista_usuarios/')