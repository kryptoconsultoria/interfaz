import requests
import os
from math import ceil
from urllib.parse import quote
import io

class MSGraphAPI:

    def __init__(self, token):
        self.token = token

    def _encode(self, path):
        return '/'.join(quote(p, safe='') for p in path.split('/'))

    def get_site_id(self, domain, site_name =''):
        """
        Obtiene el ID del sitio (site_id) de SharePoint a partir del nombre del sitio y el dominio.
        """
        url = f"https://graph.microsoft.com/v1.0/sites/{domain}:/sites/{site_name}"
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.get(url, headers=headers, verify=True)

        if response.status_code == 200:
            return response.json()["id"]
        else:
            raise Exception(
                f"Error al obtener el site_id: {response.status_code}, {response.json()}"
            )

    def list_drives(self, hostname):
        """
        Lista todas las bibliotecas de documentos (drives) de un sitio de SharePoint.
        """
        url = f"https://graph.microsoft.com/v1.0/sites/{hostname}/drives"
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.get(url, headers=headers, verify=True)

        if response.status_code == 200:
            return response.json()["value"]
        else:
            raise Exception(
                f"Error al listar drives: {response.status_code}, {response.json()}"
            )

    def delete_all_files_in_folder(self, hostname, drive_id, folder_path):
        """
        Elimina todos los archivos de una carpeta en SharePoint.
        :param hostname: Dominio del sitio de SharePoint.
        :param drive_id: ID de la biblioteca de documentos (drive).
        :param folder_path: Ruta de la carpeta dentro del drive.
        :return: Respuesta de éxito o error.
        """
        url = f"https://graph.microsoft.com/v1.0/sites/{hostname}/drives/{drive_id}/root:/{folder_path}:/children"
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.get(url, headers=headers, verify=True)

        if response.status_code == 200:
            files = response.json()["value"]
            for file in files:
                if "file" in file:  # Solo eliminar archivos
                    delete_url = f"https://graph.microsoft.com/v1.0/sites/{hostname}/drives/{drive_id}/items/{file['id']}"
                    delete_response = requests.delete(delete_url, headers=headers, verify=True)
                    if delete_response.status_code not in (200, 204):
                        raise Exception(
                            f"Error al eliminar archivo {file['name']}: {delete_response.status_code}, {delete_response.json()}"
                        )
            return {"success": True, "message": "Archivos eliminados corbuffer = io.BytesIO()rectamente."}
        else:
            raise Exception(
                f"Error al obtener archivos de la carpeta: {response.status_code}, {response.json()}"
            )

    def upload_file_to_sharepoint(self,hostname,drive_id,file_path,folder_path=""):
        """
        Sube un archivo a SharePoint utilizando sesiones de subida con manejo de archivos fragmentados.
        :param hostname: Dominio del sitio de SharePoint.
        :param drive_id: ID de la biblioteca de documentos (drive).
        :param file_path: Ruta completa del archivo a subir.
        :param folder_path: Carpeta de destino en el drive. Opcional.
        :return: Respuesta de éxito o error.
        """
        file_name = file_path.split("/")[-1]
        folder_path = folder_path + "/" if folder_path else ""
        base_url = f"https://graph.microsoft.com/v1.0/sites/{hostname}/drives/{drive_id}/root:/{folder_path}{file_name}:/createUploadSession"

        headers = {"Authorization": f"Bearer {self.token}"}
        upload_session = requests.post(base_url, headers=headers, verify=True).json()

        if "uploadUrl" not in upload_session:
            raise Exception(
                f"Error creando sesión de subida: {upload_session.get('error')}"
            )

        upload_url = upload_session["uploadUrl"]
        file_size = os.path.getsize(file_path)
        chunk_size = 327680  # 320KB por fragmento
        total_chunks = ceil(file_size / chunk_size)

        with open(file_path, "rb") as file:
            for chunk_index in range(total_chunks):
                start_byte = chunk_index * chunk_size
                end_byte = min(start_byte + chunk_size, file_size) - 1
                chunk_data = file.read(chunk_size)

                chunk_headers = {
                    "Content-Range": f"bytes {start_byte}-{end_byte}/{file_size}",
                    "Content-Type": "application/octet-stream",
                }

                response = requests.put(
                    upload_url, headers=chunk_headers, data=chunk_data, verify=True
                )

                if response.status_code not in (200, 201, 202):
                    raise Exception(
                        f"Error subiendo fragmento {chunk_index + 1}/{total_chunks}: {response.json()}"
                    )
        return {
            "success": True,
            "message": f"Archivo '{file_name}' subido correctamente en {total_chunks} fragmentos."
        }

    def download_file_from_sharepoint(self, hostname, drive_id, file_id):
        """
        Descarga un archivo desde SharePoint usando su ID de elemento.

        :param hostname: Dominio del sitio de SharePoint (p.ej., 'kryptocolombia.sharepoint.com').
        :param drive_id: ID de la biblioteca de documentos (dnrive).
        :param file_id: ID del archivo (driveItem) que se desea descargar.
        :return: dict con {"success": True, "buffer": BytesIO} si se descarga correctamente,
                 o lanza excepción en caso de error.
        """
        url = f"https://graph.microsoft.com/v1.0/sites/{hostname}/drives/{drive_id}/items/{file_id}/content"
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.get(url, headers=headers, stream=True, verify=True)
        if response.status_code == 200:
            buffer = io.BytesIO()
            for chunk in response.iter_content(chunk_size=8192):
                buffer.write(chunk)
            buffer.seek(0)
            return {"success": True, "buffer": buffer}
        else:
            raise Exception(f"Error al descargar el archivo: {response.status_code}, {response.text}")


    def list_files_folders(self,hostname,drive_id,parent_folder_path="",item_type="folder",names=None,match_all=True):
        """
        Lista las carpetas dentro de un drive en SharePoint.
        :param hostname: Dominio del sitio de SharePoint (por ejemplo, "example.sharepoint.com").
        :param drive_id: ID del drive.
        :param parent_folder_path: Ruta de la carpeta padre dentro del drive. Opcional.
        :return: Lista de carpetas en el nivel especificado.
        """

        base = f"https://graph.microsoft.com/v1.0/sites/{hostname}/drives/{drive_id}"
        url = f"{base}/root:/{parent_folder_path}:/children" if parent_folder_path else f"{base}/root/children"

        resp = requests.get(url, headers={"Authorization": f"Bearer {self.token}"})
        items = resp.json().get("value", [])

        # Ordena por fecha de creación (descendente)
        items.sort(key=lambda i: i.get("createdDateTime", ""), reverse=True)

        # Normaliza 'names' para filtrado
        if names is None:
            terms = []
        elif isinstance(names, str):
            terms = [names]
        elif isinstance(names, (list, tuple)):
            terms = names
        else:
            raise ValueError("names debe ser str, lista de str o None")


        def matches(item):
            if item_type not in item:
                return False
            nm = item.get("name", "")
            if not terms:
                return True
            checks = [term in nm for term in terms]
            return all(checks) if match_all else any(checks)

        filtered = [it for it in items if matches(it)]
        return {"success": True, "items": filtered}







