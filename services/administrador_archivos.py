from importlib.metadata import files

from .msal_client import MSGraphAuth
from .msgraph_api import MSGraphAPI
from dotenv import load_dotenv
import io
import os


class NamedBytesIO(io.BytesIO):
    """
    BytesIO que añade un atributo `name` y un método `chunks()`
    para poder usarse como sustituto de `UploadedFile` en pruebas.
    """
    def __init__(self, data: bytes, name: str):
        super().__init__(data)
        self.name = name            # atributo presente en UploadedFile

    # Django llama a chunks() varias veces para leer el archivo.
    # Aquí lo replicamos con un generador.
    def chunks(self, chunk_size: int = 8192):
        self.seek(0)                # empezamos desde el principio
        while True:
            chunk = self.read(chunk_size)
            if not chunk:
                break
            yield chunk

class AdministradorArchivos:

    def __init__(self):
        """
        Inicializa las credenciales a partir del archivo .env y configura los servicios de MSGraph.
        """
        load_dotenv()
        self.ID_CLIENTE = os.getenv("CLIENT_ID")
        self.SECRETO_CLIENTE = os.getenv("CLIENT_SECRET")
        self.ID_TENANT = os.getenv("TENANT_ID")
        self.DOMINIO = os.getenv("DOMAIN")  # Ejemplo: "contoso.sharepoint.com"
        self.NOMBRE_SITIO = os.getenv("SITE_NAME")  # Ejemplo: "contoso.sharepoint.com"
        self.TOKEN_ACTUALIZACION = os.getenv("REFRESH_TOKEN")  # Ejemplo: "obtener token"

    def borrar_archivos(self,ruta_carpeta):
        # borrar todos los archivos del sharepoint
        try:
            cliente_autenticacion = MSGraphAuth(
                self.ID_CLIENTE,
                self.SECRETO_CLIENTE,
                self.ID_TENANT,
                self.TOKEN_ACTUALIZACION
            )

            token = cliente_autenticacion.renovar_access_token()
            cliente_api = MSGraphAPI(token=token)
            # Listar unidades del sitio y encontrar la requerida
            unidades = cliente_api.list_drives(self.DOMINIO)
            id_drive = unidades[3]["id"] if unidades else None

            resultado = cliente_api.delete_all_files_in_folder(
                hostname=self.DOMINIO,
                drive_id=id_drive,
                folder_path=ruta_carpeta
            )

            if resultado.get('success'):
                return {"success": True, "message": "Archivo subido exitosamente a SharePoint."}
            else:
                return {"success": False, "message": resultado.get('error', 'Error al subir el archivo.')}
        except Exception as e:
            return {"success": False, "message": str(e)}


    def cargar_archivo(self, ruta_archivo, ruta_carpeta):
        """
        Función reutilizable para subir un archivo a SharePoint.

        Parámetros:
        - nombre_sitio: Nombre del sitio de SharePoint.
        - nombre_biblioteca: Nombre de la biblioteca de documentos.
        - nombre_archivo: Nombre del archivo a cargar.
        - contenido_archivo: Contenido del archivo (binario).

        Devuelve:
        - Un diccionario con el resultado de la carga.
        """
        try:

            # Crear cliente de Microsoft Graph
            cliente_autenticacion = MSGraphAuth(
                self.ID_CLIENTE,
                self.SECRETO_CLIENTE,
                self.ID_TENANT,
                self.TOKEN_ACTUALIZACION
            )

            token = cliente_autenticacion.renovar_access_token()
            cliente_api = MSGraphAPI(token=token)
            nombre_archivo = ruta_archivo.name
            ruta_archivo_temp = f"temp/{nombre_archivo}"


            # Guardar archivo de forma temporal en el sistema
            with open(ruta_archivo_temp, "wb+") as archivo_temporal:
                for fragmento in ruta_archivo.chunks():
                    archivo_temporal.write(fragmento)

            # Listar unidades del sitio y encontrar la requerida
            unidades = cliente_api.list_drives(self.DOMINIO)

            id_drive = unidades[3]["id"] if unidades else None

            items = cliente_api.list_files_folders(self.DOMINIO,id_drive,ruta_carpeta,"file")

            # Comprobar existencia exacta
            exists = any(item.get("name") == nombre_archivo for item in items)


            if exists:
                return {"success": True, "message": "El archivo ya existe. No se subió."}


            # Subir el archivo
            resultado = cliente_api.upload_file_to_sharepoint(
                hostname=self.DOMINIO,
                drive_id=id_drive,
                file_path=ruta_archivo_temp,
                folder_path=ruta_carpeta
            )
            if resultado.get('success'):
                return {"success": True, "message": "Archivo subido exitosamente a SharePoint."}
            else:
                return {"success": False, "message": resultado.get('error', 'Error al subir el archivo.')}

        except Exception as e:
            return {"success": False, "message": str(e)}
        finally:
            # Limpiar el archivo temporal
            if os.path.exists(ruta_archivo_temp):
                os.remove(ruta_archivo_temp)

if __name__ == "__main__":
    administrador = AdministradorArchivos()
    file_content = b"huiol"
    file_name = "archivo_simulado.txt"
    archivo_simulado = NamedBytesIO(file_content, file_name)

    administrador = AdministradorArchivos()
    res = administrador.cargar_archivo(
        ruta_archivo=archivo_simulado,
        ruta_carpeta="Innovación y Tecnología/IntegrIA/Proyectos automatización/07 Medios Magnéticos/text"
    )


