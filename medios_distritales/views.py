from django.http import FileResponse
from django.shortcuts import render
from medios_distritales.models import Cliente, Sistema, Estado
from services.administrador_archivos import AdministradorArchivos
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.safestring import mark_safe
from django.conf import settings
import os
import json
import requests

# Utilidad para estructuras de respuesta estándar
def json_response(success: bool, message: str, data=None, status=200):
    return JsonResponse({
        "success": success,
        "message": message,
        "data": data or {}
    }, status=status)

# Utilidad genérica para subir un archivo a SharePoint
# Espera que SHAREPOINT_BASE_URL_MEDIOS_DISTRITALES esté definido en settings.py, por ejemplo:
# SHAREPOINT_BASE_URL_MEDIOS_DISTRITALES = "https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents"

def manejo_archivo_subida(request, field_name, subpath, allowed_ext=None, aditional_path=''):
    file = request.FILES.get(field_name)
    if not file:
        return json_response(False, "No se recibió ningún archivo", status=400)

    cliente = request.session.get('cliente_nombre')
    if not cliente:
        return json_response(False, "Cliente no definido en sesión", status=400)

    # Construcción de la ruta completa en SharePoint
    base_url = settings.SHAREPOINT_BASE_URL_MEDIOS_DISTRITALES.rstrip('/')
    sharepoint_path = f"{base_url}/{subpath}/{cliente}{aditional_path}"

    # Validación de extensión
    ext = os.path.splitext(file.name)[1].lower()
    if allowed_ext and ext not in allowed_ext:
        return json_response(False, "Tipo de archivo no permitido", status=400)

    try:
        admin = AdministradorArchivos()
        # Se asume que cargar_archivo acepta rutas web de SharePoint o utiliza APIs internas
        result = admin.cargar_archivo(file, sharepoint_path)
        return json_response(result.get('success', False), result.get('message', ''), {"filename": file.name})
    except Exception as e:
        return json_response(False, f"Error interno: {str(e)}", status=500)

# Borrar archivos del sharepoint
def manejo_archivos_borrado(request, subpath, aditional_path=''):
    cliente = request.session.get('cliente_nombre')
    if not cliente:
        return json_response(False, "Cliente no definido en sesión", status=400)

    # Construcción de la ruta completa en SharePoint
    base_url = settings.SHAREPOINT_BASE_URL_MEDIOS_DISTRITALES.rstrip('/')
    sharepoint_path = f"{base_url}/{subpath}/{cliente}{aditional_path}"

    try:
        admin = AdministradorArchivos()
        # Se asume que cargar_archivo acepta rutas web de SharePoint o utiliza APIs internas
        result = admin.eliminar_archivos(sharepoint_path)
        return json_response(result.get('success', False), result.get('message', ''))
    except Exception as e:
        return json_response(False, f"Error interno: {str(e)}", status=500)

# Descargar archivo del sharepoint
def descargar_archivo(request,ruta_carpeta,nombres):
    cliente = request.session.get('cliente_nombre')
    if not cliente:
        return json_response(False, "Cliente no definido en sesión", status=400)
    try:
        admin = AdministradorArchivos()
        base_url = settings.SHAREPOINT_BASE_URL_MEDIOS_DISTRITALES.rstrip('/')
        sharepoint_path = f"{base_url}/{ruta_carpeta}"
        resultado = admin.descargar_ultimo_archivo(sharepoint_path,nombres)
        buffer = resultado["buffer"]
        nombre_archivo = resultado["file_name"]
        response = FileResponse(buffer, as_attachment=True, filename=nombre_archivo)
        response.headers['Access-Control-Expose-Headers'] = 'Content-Disposition'
        return response
    except Exception as e:
        return json_response(False, f"Error interno: {str(e)}", status=500)

# ==================== VISTAS GENERALES ====================

def obtener_datos_sistemas_clientes():
    sistemas = Sistema.objects.all()
    clientes = Cliente.objects.all()
    return {
        "sistemas": [{"idsistema": s.idsistema, "nombre": s.nombre} for s in sistemas],
        "clientes": [
            {"idcliente": c.idcliente, "nombre": c.nombre, "idsistema": c.idsistema_id}
            for c in clientes
        ]
    }

@csrf_exempt
def guardar_seleccion(request):
    if request.method != 'POST':
        return json_response(False, "Método no permitido", status=405)
    try:
        body = json.loads(request.body)
        sistema = body.get("sistema")
        cliente = body.get("cliente")
        if not sistema or not cliente:
            return json_response(False, "Datos incompletos", status=400)
        request.session['sistema_nombre'] = sistema.get("nombre")
        request.session['cliente_nombre'] = cliente.get("nombre")
        return json_response(True, "Selección guardada")
    except Exception as e:
        return json_response(False, f"Error interno: {str(e)}", status=500)

@login_required
def medios_distritales(request):
    if request.user.perfil.tiene_acceso_a("medios_distritales"):
        data = obtener_datos_sistemas_clientes()
        return render(request, 'medios_distritales/base.html', {'initial_data': mark_safe(json.dumps(data))})
    return render(request, 'acceso_denegado.html')

def iniciar_automatizacion_distritales(request):
    try:
        cliente_nombre = request.session.get('cliente_nombre')
        if not cliente_nombre:
            return json_response(False, "Faltan datos de cliente o sistema", status=400)
        payload = {"cliente": cliente_nombre, "usuario": request.user.username}
        print('estoy llamando distritales')
        resp = requests.post(f"{settings.FASTAPI_URL}medios_distritales", json=payload)
        if resp.status_code == 200:
            data = resp.json()
            return json_response(True,"Automatizacion iniciada exitosamente",data=data,status=200)
        else:
            return json_response(False, "Error al iniciar automatización", status=500)
    except Exception as e:
        return json_response(False, f"Error interno: {str(e)}", status=500)


# ==================== ENDPOINTS DE SUBIDA ====================
@csrf_exempt
@login_required
@require_POST
def puc_distritales(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents/insumos/puc_exogena
    return manejo_archivo_subida(request, 'archivo', 'insumos/puc_exogena',['.csv'])

@csrf_exempt
@login_required
@require_POST
def rete_ica_terceros(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents/insumos/rete_ica_terceros/{cliente}
    return manejo_archivo_subida(request, 'archivo', 'insumos/rete_ica_terceros', ['.pdf'])

@csrf_exempt
@login_required
@require_POST
def rete_ica(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents/insumos/rete_ica_terceros/{cliente}
    return manejo_archivo_subida(request, 'archivo', 'insumos/rete_ica', ['.pdf'])

@csrf_exempt
@login_required
@require_POST
def balances_distritales(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents/insumos/insumos_{sistema}/balance_terceros/{cliente}
    sistema = request.session.get('sistema_nombre')
    return manejo_archivo_subida(request, 'archivo', f'insumos/insumos_{sistema}',aditional_path=f'/balance_terceros')

@csrf_exempt
@login_required
@require_POST
def terceros_distritales(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents/insumos/insumos_{sistema}/modelo_terceros/{cliente}
    sistema = request.session.get('sistema_nombre')
    return manejo_archivo_subida(request, 'archivo', f'insumos/insumos_{sistema}/modelo_terceros',aditional_path=f'/listado_terceros')

@csrf_exempt
@login_required
@require_POST
def anexo_ica(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents/insumos/insumos_{sistema}/anexo_ica/{cliente}
    sistema = request.session.get('sistema_nombre')
    return manejo_archivo_subida(request, 'archivo', f'insumos/anexo_ica')


# ==================== ENDPOINTS DE BORRADO ====================
@csrf_exempt
@login_required
@require_POST
def puc_distritales_borrado(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents/insumos/puc_exogena
    return manejo_archivos_borrado(request,  'insumos/puc_exogena')

@csrf_exempt
@login_required
@require_POST
def balances_distritales_borrado(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents/insumos/insumos_{sistema}/balance_terceros/{cliente}
    sistema = request.session.get('sistema_nombre')
    return manejo_archivos_borrado(request, f'insumos/insumos_{sistema}',aditional_path=f'/balance_terceros')

@csrf_exempt
@login_required
@require_POST
def terceros_distritales_borrado(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents/insumos/insumos_{sistema}/modelo_terceros/{cliente}
    sistema = request.session.get('sistema_nombre')
    return manejo_archivos_borrado(request, f'insumos/insumos_{sistema}',aditional_path=f'/listado_terceros')

@csrf_exempt
@login_required
@require_POST
def rete_ica_terceros_borrado(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents/insumos/rete_ica_terceros/{cliente}
    return manejo_archivos_borrado(request, 'insumos/rete_ica_terceros')

@csrf_exempt
@login_required
@require_POST
def rete_ica_borrado(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents/insumos/rete_ica_terceros/{cliente}
    return manejo_archivos_borrado(request, 'insumos/rete_ica')

@csrf_exempt
@login_required
@require_POST
def anexo_ica_borrado(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents/insumos/anexo_ica_borrado/{cliente}
    return manejo_archivos_borrado(request, 'insumos/anexo_ica_borrado')

# ==================== ENDPOINTS DE DESCARGA ====================
@csrf_exempt
@login_required
@require_POST
def descargar_medios_distritales(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_distritales/Shared Documents/insumos/salidas/
    usuario = request.user.username
    cliente = request.session.get('cliente_nombre')
    return descargar_archivo(request,'salidas',[cliente,usuario,'desglosado'])
