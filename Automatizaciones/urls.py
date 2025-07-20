"""
URL configuration for Automatizaciones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.views.generic import RedirectView

from panel_principal.views import *
from medios_magneticos.views import *
from panel_principal.forms.login_form import LoginForm

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Autenticación
    path('', auth_views.LoginView.as_view(
        template_name='componentes_login/login.html',
        authentication_form=LoginForm,
        success_url=reverse_lazy('medios_magneticos'),
        redirect_authenticated_user=True
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='logout_success'
    ), name='logout'),

    path('logout_success/', TemplateView.as_view(
        template_name='logout.html'
    ), name='logout_success'),

    # Recuperación de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='componentes_login/password_reset.html'
    ), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='componentes_login/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='componentes_login/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),

    #Panel principal
    path('panel_principal/', RedirectView.as_view(url='/medios_magneticos/', permanent=False),name='index'),

    # Medios magnéticos
    path("<str:prefijo>/obtener_sistemas_clientes/", obtener_datos_sistemas_clientes,
         name="obtener_datos_sistemas_clientes"),

    path('medios_magneticos/guardar_seleccion/', guardar_seleccion, name='guardar_seleccion'),
    path('medios_magneticos/', medios_magneticos, name='medios_magneticos'),
    # ===================================================================================================================
    # SUBIDA DE ARCHIVOS EN CADA ENDPOINT
    # ===================================================================================================================
    path('medios_magneticos/balances/', balances, name='balances'),
    path('medios_magneticos/terceros/', terceros, name='terceros'),
    path('medios_magneticos/puc/', puc, name='puc'),
    path('medios_magneticos/anexos_renta/', anexos, name='anexos'),
    path('medios_magneticos/participacion_accionaria/', participacion_accionaria, name='participacion_accionaria'),
    path('medios_magneticos/planillas/', planillas, name='planillas'),
    path('medios_magneticos/ingresos_retenciones/', ingresos_retenciones, name='ingresos_retenciones'),
    path('medios_magneticos/retenciones_fuente/', retenciones_fuente, name='retenciones_fuente'),
    path('medios_magneticos/iniciar_automatizacion/', iniciar_automatizacion, name='iniciar_automatizacion'),
    #===================================================================================================================
    # BORRADO DE ARCHIVOS EN CADA ENDPOINT
    # ===================================================================================================================
    path('medios_magneticos/balances_borrado/', balances_borrado, name='balances_borrado'),
    path('medios_magneticos/terceros_borrado/', terceros_borrado, name='terceros_borrado'),
    path('medios_magneticos/puc_borrado/', puc_borrado, name='puc_borrado'),
    path('medios_magneticos/anexos_renta_borrado/', anexos_borrado, name='anexos_borrado'),
    path('medios_magneticos/participacion_accionaria_borrado/', participacion_accionaria_borrado, name='participacion_accionaria_borrado'),
    path('medios_magneticos/planillas_borrado/', planillas_borrado, name='planillas_borrado'),
    path('medios_magneticos/ingresos_retenciones_borrado/', ingresos_retenciones_borrado, name='ingresos_retenciones_borrado'),
    path('medios_magneticos/retenciones_fuente_borrado/', retenciones_fuente_borrado, name='retenciones_fuente_borrado'),
    # ===================================================================================================================
    # DESCARGA DE ARCHIVOS
    # ===================================================================================================================
    path('medios_magneticos/descargar_puc/', descargar_puc,name='descargar_puc'),
    path('medios_magneticos/descargar_medios_desglosados/', descargar_medios_desglosados,name='descargar_medios_desglosados'),
    path('medios_magneticos/descargar_medios/', descargar_medios,name='descargar_medios'),
]
