"""
URL configuration for super project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from superApp import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main),
    path('categoria/',views.categoria),
    path('gestion/',views.gestion),
    path('contacto/',views.contacto),
    path('productos/<str:categoria>/',views.producto),
    path('login/',views.login_user),
    path('logout_user/',views.logout_user),
    path('editar_producto/<int:id>/',views.editar_producto),
    path('eliminar_producto/<int:id>/',views.eliminar_producto),
    path('perfil/<int:id>/',views.perfil),
    path('agradecimiento/',views.agradecimiento),
    path('formularios/',views.vista_formulario),
    path('eliminar_formulario/<int:id>/',views.eliminar_formulario),
    path('detalles/<int:id>/',views.detalles),
    path('aprobar/<int:id>/',views.aprobar),
    path('crear_usuario/',views.crear_usuario),
    path('lista_usuarios/',views.lista_usuarios),
    path('eliminar_usuario/<int:id>/',views.eliminar_usuario),
    path('cambiar_admin/<int:id>/',views.cambiar_admin),
    path('cambiar_estandar/<int:id>/',views.cambiar_estandar),
    path('restablecer_contraseña/<int:id>/',views.restablecer_contraseña)
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)