from django.shortcuts import render
from medios_magneticos.models import Cliente,Sistema
from services.administrador_archivos import AdministradorArchivos
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed,HttpResponseBadRequest
import os
import json
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import requests
from django.http import JsonResponse
from django.forms.models import model_to_dict
from medios_magneticos.models import Estado


# Utilidad para estructuras de respuesta estándar
def json_response(success: bool, message: str, data=None, status=200):
    return JsonResponse({
        "success": success,
        "message": message,
        "data": data if data else []
    }, status=status)

# Utilidad para estructurar la subida de los multiples archivos
def subir_multiples_archivos(aceptados,archivos,ruta_carpeta,extensiones_admitidas):
    try:
        archivos_guardados = []
        archivos_rechazados = []
        for f in archivos:
            ext = os.path.splitext(f.name)[1].lower()
            if extensiones_admitidas and ext not in extensiones_admitidas:
                archivos_rechazados.append(f.name)
                continue
            admin_arch = AdministradorArchivos()
            resultado = admin_arch.cargar_archivo(f, ruta_carpeta)
            archivos_guardados.append(f.name)
        if archivos_rechazados:
            return JsonResponse({
                "error": "Algunos archivos fueron rechazados por tipo de archivo no permitido",
                "rejected": archivos_rechazados
            }, status=400)

        return JsonResponse({
            "message": "Archivos subidos exitosamente",
            "files": archivos_guardados
        })
    except Exception as e:
        return json_response(False, f"Error: {str(e)}", status=500)


# Create your views here.
# Endpoint para obtener sistemas y clientes
def obtener_datos_sistemas_clientes():
    sistemas = Sistema.objects.all()
    clientes = Cliente.objects.all()

    sistemas_data = [{"idsistema": s.idsistema, "nombre": s.nombre} for s in sistemas]
    clientes_data = [
        {
            "idcliente": c.idcliente,
            "nombre": c.nombre,
            "idsistema": c.idsistema_id  # clave para filtrar en Vue
        }
        for c in clientes
    ]
    return {
        "sistemas": sistemas_data,
        "clientes": clientes_data
    }
@csrf_exempt
def guardar_seleccion(request):
    if request.method == 'POST':
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
            return json_response(False, f"Error: {str(e)}", status=500)
    return json_response(False, "Método no permitido", status=405)

@login_required
def medios_magneticos(request):
    if request.user.perfil.tiene_acceso_a("medios_magneticos"):
        data = obtener_datos_sistemas_clientes()
        context = {
            'initial_data': mark_safe(json.dumps(data))
        }
        return render(request, 'medios_magneticos/base.html',context)
    else:
        return render(request, 'acceso_denegado.html')

# Vista para traer el estado actual de la automatizacion
def estado_automatizacion(request):
    estado_data = Estado.objects.order_by('idestado').last()
    if estado_data:
        # Convertir el objeto Estado a un diccionario
        estado_serializado = model_to_dict(estado_data)
        return JsonResponse({"estado": "exitoso", "detalle": estado_serializado})
    else:
        # Si no existe un estado en la base de datos
        return JsonResponse({"estado": None,"detalle": None})



def iniciar_automatizacion(request):
    try:
        # Obtener nombres del sistema y cliente de la sesión
        cliente_nombre = request.session.get('cliente_nombre')

        if not cliente_nombre:
            return JsonResponse({
                "estado": "error",
                "detalle": {"mensaje": "Faltan datos de cliente o sistema"}
            }, status=400)

        # Llamar al endpoint FastAPI (ajusta la URL real de tu servidor)
        fastapi_url = "http://localhost:40/medios_magneticos"
        payload = {
            "cliente": cliente_nombre,
            "usuario": "admin"
        }
        response = requests.post(fastapi_url, json=payload)

        if response.status_code == 200:
            fastapi_data = response.json()
        else:
            fastapi_data = {
                "mensaje": "Error al ejecutar FastAPI",
                "codigo": response.status_code
            }

        return JsonResponse({
            "estado": "success",
            "detalle": {
                "respuesta_fastapi": fastapi_data
            }
        })

    except Exception as e:
        return JsonResponse({
            "estado": "error",
            "detalle": {"mensaje": f"Error interno: {str(e)}"}
        }, status=500)

@csrf_exempt
@login_required
@require_POST
def puc(request):
    try:
        ruta_archivo = request.FILES.get('archivo')
        ruta_carpeta = f"Innovación y Tecnología/IntegrIA/Proyectos automatización/07 Medios Magnéticos/insumos/puc_exogena"
        admin_arch = AdministradorArchivos()
        resultado = admin_arch.cargar_archivo(ruta_archivo, ruta_carpeta)
        return json_response(resultado.get('success', False), resultado.get('message', ''))
    except (Sistema.DoesNotExist, Cliente.DoesNotExist):
        return json_response(False, "Sistema o cliente no encontrado", status=404)
    except Exception as e:
        return json_response(False, f"Error: {str(e)}", status=500)


@csrf_exempt
@login_required
def retenciones_fuente(request):
    if request.method == 'POST':
        try:
            cliente_nombre = request.session.get('cliente_nombre')
            if not cliente_nombre:
                return json_response(False, "Sistema y cliente son requeridos", status=400)

            archivos = request.FILES.getlist('archivos[]')
            if not archivos:
                return json_response(False, "No se recibieron archivos", status=400)

            aceptados = request.GET.get('accept')
            ruta_carpeta = f"Innovación y Tecnología/IntegrIA/Proyectos automatización/07 Medios Magnéticos/insumos/pdf_1003/{cliente_nombre}"
            extensiones_admitidas = ['.pdf']
            return subir_multiples_archivos(aceptados, archivos, ruta_carpeta, extensiones_admitidas)
        except Exception as e:
            return json_response(False, f"Error: {str(e)}", status=500)

    # Si no es POST, devolver explícitamente 405
    return HttpResponseNotAllowed(['POST'])


@csrf_exempt
@login_required
def planillas(request):
    if request.method == 'POST':
        try:
            cliente_nombre = request.session.get('cliente_nombre')
            if not cliente_nombre:
                return json_response(False, "Sistema y cliente son requeridos", status=400)
            archivos = request.FILES.getlist('archivos[]')
            aceptados = request.GET.get('accept')  # parametros de tipo de archivos aceptados
            ruta_carpeta = f"Innovación y Tecnología/IntegrIA/Proyectos automatización/07 Medios Magnéticos/insumos/pdf_1003/{cliente_nombre}"
            # Aceptar únicamente archivos PDF
            extensiones_admitidas = ['.xlsx','.pdf']
            return subir_multiples_archivos(aceptados, archivos, ruta_carpeta, extensiones_admitidas)
        except Exception as e:
            return json_response(False, f"Error: {str(e)}", status=500)


@csrf_exempt
@login_required
def anexos(request):
    if request.method == 'POST':
        try:
            cliente_nombre = request.session.get('cliente_nombre')
            ruta_archivo = request.FILES.get('archivo')
            ruta_carpeta = f"Innovación y Tecnología/IntegrIA/Proyectos automatización/07 Medios Magnéticos/insumos/anexos/{cliente_nombre}"
            admin_arch = AdministradorArchivos()
            result = admin_arch.cargar_archivo(ruta_archivo, ruta_carpeta)
            return JsonResponse(result)
        except Exception as e:
            return json_response(False, f"Error: {str(e)}", status=500)

@csrf_exempt
@login_required
def balances(request):
    if request.method == 'POST':
        try:
            sistema_nombre = request.session.get('sistema_nombre')
            cliente_nombre = request.session.get('cliente_nombre')
            ruta_archivo = request.FILES.get('archivo')
            ruta_carpeta = f"Innovación y Tecnología/IntegrIA/Proyectos automatización/07 Medios Magnéticos/insumos/insumos_{sistema_nombre}/{cliente_nombre}/balance_terceros"
            admin_arch = AdministradorArchivos()
            resultado = admin_arch.cargar_archivo(ruta_archivo, ruta_carpeta)
            return json_response(resultado.get('success', False), resultado.get('message', ''))
        except Exception as e:
            return json_response(False, f"Error: {str(e)}", status=500)

@csrf_exempt
@login_required
def terceros(request):
    if request.method == 'POST':
        try:
            sistema_nombre = request.session.get('sistema_nombre')
            cliente_nombre = request.session.get('cliente_nombre')
            ruta_archivo = request.FILES.get('archivo')
            if not ruta_archivo:
                return HttpResponseBadRequest("No file uploaded")
            ruta_carpeta = f"Innovación y Tecnología/IntegrIA/Proyectos automatización/07 Medios Magnéticos/insumos/insumos_{sistema_nombre}/{cliente_nombre}/modelo_terceros"
            admin_arch = AdministradorArchivos()
            resultado = admin_arch.cargar_archivo(ruta_archivo, ruta_carpeta)
            return json_response(resultado.get('success', False), resultado.get('message', ''))
        except (Sistema.DoesNotExist, Cliente.DoesNotExist):
            return json_response(False, "Sistema o cliente no encontrado", status=404)
        except Exception as e:
            return json_response(False, f"Error: {str(e)}", status=500)



@csrf_exempt
@login_required
def participacion_accionaria(request):
    if request.method == 'POST':
        try:
            cliente_nombre = request.session.get('cliente_nombre')
            if not cliente_nombre:
                return json_response(False, "Sistema y cliente son requeridos", status=400)
            ruta_archivo = request.FILES.get('ParticipacionAccionaria')
            ruta_carpeta = f"Innovación y Tecnología/IntegrIA/Proyectos automatización/07 Medios Magnéticos/insumos/pdf_1010/{cliente_nombre}"
            admin_arch = AdministradorArchivos()
            resultado = admin_arch.cargar_archivo(ruta_archivo, ruta_carpeta)
            return json_response(resultado.get('success', False), resultado.get('message', ''))
        except Exception as e:
            return json_response(False, f"Error: {str(e)}", status=500)


# Vista para subir múltiples PDFs de ingresos y retenciones
@csrf_exempt
@login_required
@require_POST
def ingresos_retenciones(request):
    # Solo POST está permitido
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    try:
        # Obtener cliente de la sesión
        cliente_nombre = request.session.get('cliente_nombre')
        if not cliente_nombre:
            return json_response(False, "Sistema y cliente son requeridos", status=400)

        archivos = request.FILES.getlist('archivos[]')
        if not archivos:
            return json_response(False, "No se recibieron archivos", status=400)

        ruta_carpeta = f"Innovación y Tecnología/IntegrIA/Proyectos automatización/07 Medios Magnéticos/insumos/pdf_2276/{cliente_nombre}"
        extensiones_admitidas = ['.pdf']

        return subir_multiples_archivos(None, archivos, ruta_carpeta, extensiones_admitidas)
    except Exception as e:
        return json_response(False, f"Error: {str(e)}", status=500)


