from django.shortcuts import render
from medios_magneticos.models import Cliente, Sistema, Estado
from services.administrador_archivos import AdministradorArchivos
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict
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
# Espera que SHAREPOINT_BASE_URL_MEDIOS esté definido en settings.py, por ejemplo:
# SHAREPOINT_BASE_URL_MEDIOS = "https://empresa.sharepoint.com/sites/medios_magneticos/Shared Documents"

def handle_file_upload(request, field_name, subpath, allowed_ext=None):
    file = request.FILES.get(field_name)
    if not file:
        return json_response(False, "No se recibió ningún archivo", status=400)

    cliente = request.session.get('cliente_nombre')
    if not cliente:
        return json_response(False, "Cliente no definido en sesión", status=400)

    # Construcción de la ruta completa en SharePoint
    base_url = settings.SHAREPOINT_BASE_URL_MEDIOS.rstrip('/')
    sharepoint_path = f"{base_url}/{subpath}/{cliente}"

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
def medios_magneticos(request):
    if request.user.perfil.tiene_acceso_a("medios_magneticos"):
        data = obtener_datos_sistemas_clientes()
        return render(request, 'medios_magneticos/base.html', {'initial_data': mark_safe(json.dumps(data))})
    return render(request, 'acceso_denegado.html')

def estado_automatizacion(request):
    estado_data = Estado.objects.order_by('idestado').last()
    detalle = model_to_dict(estado_data) if estado_data else None
    return JsonResponse({"estado": "exitoso" if detalle else None, "detalle": detalle})

def iniciar_automatizacion(request):
    try:
        cliente_nombre = request.session.get('cliente_nombre')
        if not cliente_nombre:
            return json_response(False, "Faltan datos de cliente o sistema", status=400)
        fastapi_url = settings.FASTAPI_URL
        payload = {"cliente": cliente_nombre, "usuario": request.user.username}
        resp = requests.post(fastapi_url, json=payload)
        data = resp.json() if resp.status_code == 200 else {"mensaje": "Error FastAPI", "codigo": resp.status_code}
        return json_response(True, "Automatización iniciada", {"respuesta_fastapi": data})
    except Exception as e:
        return json_response(False, f"Error interno: {str(e)}", status=500)

# ==================== ENDPOINTS DE SUBIDA ====================

@csrf_exempt
@login_required
@require_POST
def puc(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_magneticos/Shared Documents/insumos/puc_exogena
    return handle_file_upload(request, 'archivo', 'insumos/puc_exogena',['.csv'])

@csrf_exempt
@login_required
@require_POST
def retenciones_fuente(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_magneticos/Shared Documents/insumos/pdf_1003/{cliente}
    return handle_file_upload(request, 'archivo', 'insumos/pdf_1003', ['.pdf'])

@csrf_exempt
@login_required
@require_POST
def planillas(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_magneticos/Shared Documents/insumos/pdf_1003/{cliente}
    return handle_file_upload(request, 'archivo', 'insumos/pdf_1003', ['.pdf', '.xlsx'])

@csrf_exempt
@login_required
@require_POST
def anexos(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_magneticos/Shared Documents/insumos/anexos/{cliente}
    return handle_file_upload(request, 'archivo', 'insumos/anexos')

@csrf_exempt
@login_required
@require_POST
def balances(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_magneticos/Shared Documents/insumos/insumos_{sistema}/balance_terceros/{cliente}
    sistema = request.session.get('sistema_nombre')
    return handle_file_upload(request, 'archivo', f'insumos/insumos_{sistema}/balance_terceros')

@csrf_exempt
@login_required
@require_POST
def terceros(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_magneticos/Shared Documents/insumos/insumos_{sistema}/modelo_terceros/{cliente}
    sistema = request.session.get('sistema_nombre')
    return handle_file_upload(request, 'archivo', f'insumos/insumos_{sistema}/modelo_terceros')

@csrf_exempt
@login_required
@require_POST
def participacion_accionaria(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_magneticos/Shared Documents/insumos/pdf_1010/{cliente}
    return handle_file_upload(request, 'archivo', 'insumos/pdf_1010')

@csrf_exempt
@login_required
@require_POST
def ingresos_retenciones(request):
    # Ruta de SharePoint: https://empresa.sharepoint.com/sites/medios_magneticos/Shared Documents/insumos/pdf_2276/{cliente}
    return handle_file_upload(request, 'archivo', 'insumos/pdf_2276', ['.pdf'])
