from django.contrib import admin
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView, RedirectView

from panel_principal.views import *
from medios_magneticos.views import *
from medios_distritales.views import *
from panel_principal.forms.login_form import LoginForm

urlpatterns = [
    # ==================== ADMIN ====================
    path('admin/', admin.site.urls),

    # ==================== AUTENTICACIÓN ====================
    path('', auth_views.LoginView.as_view(
        template_name='componentes_login/login.html',
        authentication_form=LoginForm,
        success_url=reverse_lazy('medios_magneticos'),
        redirect_authenticated_user=True
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='logout_success'), name='logout'),

    path('logout_success/', TemplateView.as_view(template_name='logout.html'), name='logout_success'),

    # Recuperación de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='componentes_login/password_reset.html'), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='componentes_login/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='componentes_login/password_reset_confirm.html'), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    # ==================== PANEL PRINCIPAL ====================
    path('panel_principal/', RedirectView.as_view(url='/medios_magneticos/', permanent=False), name='index'),

    # ==================== MEDIOS MAGNÉTICOS ====================
    path('medios_magneticos/', medios_magneticos, name='medios_magneticos'),
    path('medios_magneticos/guardar_seleccion/', guardar_seleccion, name='guardar_seleccion'),
    path('medios_magneticos/iniciar_automatizacion/', iniciar_automatizacion_nacionales, name='iniciar_automatizacion_nacionales'),

    # Subida
    path('medios_magneticos/balances_nacionales/', balances_nacionales, name='balances'),
    path('medios_magneticos/terceros_nacionales/', terceros_nacionales, name='terceros'),
    path('medios_magneticos/puc/', puc, name='puc'),
    path('medios_magneticos/anexos_renta/', anexos, name='anexos'),
    path('medios_magneticos/participacion_accionaria/', participacion_accionaria, name='participacion_accionaria'),
    path('medios_magneticos/planillas/', planillas, name='planillas'),
    path('medios_magneticos/ingresos_retenciones/', ingresos_retenciones, name='ingresos_retenciones'),
    path('medios_magneticos/retenciones_fuente/', retenciones_fuente, name='retenciones_fuente'),

    # Borrado
    path('medios_magneticos/balances_nacionales_borradp/', balances_nacionales_borrado, name='balances_borrado_nacionales'),
    path('medios_magneticos/terceros_nacionales_borrado/', terceros_nacionales_borrado, name='terceros_borrado_nacionales'),
    path('medios_magneticos/puc_borrado/', puc_borrado, name='puc_borrado'),
    path('medios_magneticos/anexos_renta_borrado/', anexos_borrado, name='anexos_borrado'),
    path('medios_magneticos/participacion_accionaria_borrado/', participacion_accionaria_borrado, name='participacion_accionaria_borrado'),
    path('medios_magneticos/planillas_borrado/', planillas_borrado, name='planillas_borrado'),
    path('medios_magneticos/ingresos_retenciones_borrado/', ingresos_retenciones_borrado, name='ingresos_retenciones_borrado'),
    path('medios_magneticos/retenciones_fuente_borrado/', retenciones_fuente_borrado, name='retenciones_fuente_borrado'),

    # Descarga
    path('medios_magneticos/descargar_puc/', descargar_puc, name='descargar_puc'),
    path('medios_magneticos/descargar_medios_desglosados/', descargar_medios_desglosados, name='descargar_medios_desglosados'),
    path('medios_magneticos/descargar_medios/', descargar_medios, name='descargar_medios'),

    # ==================== MEDIOS DISTRITALES ====================
    path('medios_distritales/', medios_distritales, name='medios_distritales'),
    path('medios_distritales/guardar_seleccion/', guardar_seleccion, name='guardar_seleccion_distritales'),
    path('medios_distritales/iniciar_automatizacion/', iniciar_automatizacion_distritales, name='iniciar_distritales'),

    # Subida
    path('medios_distritales/puc/', puc, name='puc_distritales'),
    path('medios_distritales/rete_ica_terceros/', rete_ica_terceros, name='rete_ica_terceros'),
    path('medios_distritales/rete_ica/', rete_ica, name='rete_ica'),
    path('medios_distritales/balances/', balances_distritales, name='balances_distritales'),
    path('medios_distritales/terceros/', terceros_distritales, name='terceros_distritales'),
    path('medios_distritales/anexo_ica/', anexo_ica, name='anexo_ica'),

    # Borrado
    path('medios_distritales/puc_borrado/', puc_distritales_borrado, name='puc_borrado_distritales'),
    path('medios_distritales/balances_distritales_borrado/', balances_distritales_borrado, name='balances_borrado_distritales'),
    path('medios_distritales/terceros_distritales_borrado/', terceros_distritales_borrado, name='terceros_borrado_distritales'),
    path('medios_distritales/rete_ica_terceros_borrado/', rete_ica_terceros_borrado, name='rete_ica_terceros_borrado'),
    path('medios_distritales/rete_ica_borrado/', rete_ica_borrado, name='rete_ica_borrado'),
    path('medios_distritales/anexo_ica_borrado/', anexo_ica_borrado, name='anexo_ica_borrado'),

    # Descarga
    path('medios_distritales/descargar/', descargar_medios_distritales, name='descargar_medios_distritales'),

    # ==================== DATOS INICIALES ====================
    path('<str:prefijo>/obtener_sistemas_clientes/', obtener_datos_sistemas_clientes, name='obtener_datos_sistemas_clientes'),
]