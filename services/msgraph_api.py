import requests
import os
from math import ceil
from urllib.parse import quote
from .msal_client import MSGraphAuth

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
    def list_files_folders(self, hostname, drive_id, parent_folder_path="",item_type="folder"):
        """
        Lista las carpetas dentro de un drive en SharePoint.
        :param hostname: Dominio del sitio de SharePoint (por ejemplo, "example.sharepoint.com").
        :param drive_id: ID del drive.
        :param parent_folder_path: Ruta de la carpeta padre dentro del drive. Opcional.
        :return: Lista de carpetas en el nivel especificado.
        """
        if parent_folder_path:
            url = f"https://graph.microsoft.com/v1.0/sites/{hostname}/drives/{drive_id}/root:/{parent_folder_path}:/children"
        else:
            url = f"https://graph.microsoft.com/v1.0/sites/{hostname}/drives/{drive_id}/root/children"

        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.get(url, headers=headers, verify=True)

        if response.status_code == 200:
            # Filtrar solo carpetas de los elementos devueltos
            folders = [
                item for item in response.json()["value"] if item[item_type]
            ]
            return folders
        else:
            raise Exception(
                f"Error al listar carpetas: {response.status_code}, {response.json()}"
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
            return {"success": True, "message": "Archivos eliminados correctamente."}
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

    def download_file_from_sharepoint(self, hostname, drive_id, file_path, download_to):
        """
        Descarga un archivo desde SharePoint a una ruta local.
        :param hostname: Dominio del sitio de SharePoint (e.g., 'kryptocolombia.sharepoint.com').
        :param drive_id: ID de la biblioteca de documentos (drive).
        :param file_path: Ruta del archivo dentro del drive (e.g., 'folder1/folder2/file.pdf').
        :param download_to: Ruta local donde se guardará el archivo descargado.
        :return: Ruta local del archivo descargado si fue exitoso.
        """
        encoded_path = self._encode(file_path)
        url = f"https://graph.microsoft.com/v1.0/sites/{hostname}/drives/{drive_id}/root:/{encoded_path}:/content"
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.get(url, headers=headers, stream=True, verify=True)

        if response.status_code == 200:
            with open(download_to, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return {"success": True, "message": f"Archivo descargado correctamente en {download_to}"}
        else:
            raise Exception(
                f"Error al descargar el archivo: {response.status_code}, {response.text}"
            )

if __name__ == "__main__":
    #auth_client = MSGraphAuth("952ce091-2362-481e-aa37-61325d6f2e0f","jjk8Q~9~wfmhW4b-N2FDX1dY7mT1_gvgH0Kivc7y","a177ae79-1984-4633-97c2-db990f28feef")
    # Inicia flujo interactivo de autenticación
    #token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IkVXUWNXMS1xYW1VVXdTQXF1eFo0NGlQMHBMNmI5SFVZclRxdW9oNUZYSVEiLCJhbGciOiJSUzI1NiIsIng1dCI6IkNOdjBPSTNSd3FsSEZFVm5hb01Bc2hDSDJYRSIsImtpZCI6IkNOdjBPSTNSd3FsSEZFVm5hb01Bc2hDSDJYRSJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9hMTc3YWU3OS0xOTg0LTQ2MzMtOTdjMi1kYjk5MGYyOGZlZWYvIiwiaWF0IjoxNzQ2NzIyMTcxLCJuYmYiOjE3NDY3MjIxNzEsImV4cCI6MTc0NjcyNzIwNCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFYUUFpLzhaQUFBQSs2dC85bmlxSmRGUHlXV25xSGo1S3lwNnNucmM2MSs2VUc5dkhCYkpKRXRLaEJhOTdaTGtPYmFQd1hIVmF1K2p6WHUrR1NpN2tjcXB6VjFWYU8zZXkyTWN0ajUrRWp2VGZkVVh1ZEw5MTh2aldIS2hnLzJPOWNBQ0xxcElXOVhXRk04dmEwdGVvK29lMGdudlZKTUlpZz09IiwiYW1yIjpbInB3ZCIsInJzYSJdLCJhcHBfZGlzcGxheW5hbWUiOiJBcHAgTWVkaW9zX21hZ25ldGljb3MiLCJhcHBpZCI6Ijk1MmNlMDkxLTIzNjItNDgxZS1hYTM3LTYxMzI1ZDZmMmUwZiIsImFwcGlkYWNyIjoiMSIsImRldmljZWlkIjoiOTM4N2EyM2EtOWM2OS00MDk0LTg1NGMtMTI2ZDExZjJiODJjIiwiZmFtaWx5X25hbWUiOiJDYXN0YcOxbyBNYXJ0aW5leiIsImdpdmVuX25hbWUiOiJPc2NhciBGZWxpcGUiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyODAwOmU2OjEwMTA6YmQzMToxYzgxOmJiOGM6ZGZhNjpjOGQ0IiwibmFtZSI6IkZlbGlwZSBDYXN0YcOxbyBNYXJ0aW5leiIsIm9pZCI6ImQ3NjA5OWMzLTlmOGUtNGI0NS05ZjE1LTk0NDY4ODVkOWVlOCIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwNDMzNERGRTQ4IiwicmgiOiIxLkFUUUFlYTUzb1lRWk0wYVh3dHVaRHlqLTd3TUFBQUFBQUFBQXdBQUFBQUFBQUFCUUFYazBBQS4iLCJzY3AiOiJGaWxlcy5SZWFkLkFsbCBGaWxlcy5SZWFkV3JpdGUuQWxsIEZpbGVzLlJlYWRXcml0ZS5BcHBGb2xkZXIgRmlsZXMuU2VsZWN0ZWRPcGVyYXRpb25zLlNlbGVjdGVkIE15RmlsZXMuUmVhZCBNeUZpbGVzLldyaXRlIFNpdGVzLlJlYWQuQWxsIFNpdGVzLlJlYWRXcml0ZS5BbGwgU2l0ZXMuU2VhcmNoLkFsbCBVc2VyLlJlYWQgVXNlci5SZWFkLkFsbCBVc2VyLlJlYWRXcml0ZS5BbGwgcHJvZmlsZSBvcGVuaWQgZW1haWwiLCJzaWQiOiIwMDIxOTlhOS0zNzk2LWU1MGEtNGVmNC05YzY5MWVmNWM4MzQiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiIzTEhIV2sxQ3gxV2dXZjV2eHpwSUdqYXREbjNwWFBUUEkwVUpkSnBrYnhzIiwidGVuYW50X3JlZ2lvbl9zY29wZSI6IlNBIiwidGlkIjoiYTE3N2FlNzktMTk4NC00NjMzLTk3YzItZGI5OTBmMjhmZWVmIiwidW5pcXVlX25hbWUiOiJmZWxpcGUuY2FzdGFub0BrcnlwdG8uY29tLmNvIiwidXBuIjoiZmVsaXBlLmNhc3Rhbm9Aa3J5cHRvLmNvbS5jbyIsInV0aSI6InR2b3hUdlZUMkUtMm9NdXplU1FSQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfaWRyZWwiOiIxIDE2IiwieG1zX3N0Ijp7InN1YiI6InpDdExZclNyVHdRTzBHbVY4WlhNTy1naml6a3hkNXU4ZzJPYTg1eEVYZkkifSwieG1zX3RjZHQiOjE0NDI0OTk2MjN9.MaXfGDWbGun6EGo8BmVI9zzacIeDR-RBs9i4sumYy-7bSKS8eK9l5ztrrVKvtd55lI1MdxcImHiUV-W6RBXVixOLr6WB_3CauzAAcZFsbiIJmgMIoyU2-H5IygpNQBBgGkjOkGTz2BSGUiJIAGyiBWRoUEJZdNUipalda5SbycMCZcb0yEDd2TJIUqK9okIhqG-rRbF4Hv-ggFzXrttoMZXFJ1miAceIiB_Lcsdf6DY98KiOMz41GvzDvC8VdjksvP7g7WIAjoNitCV5jeLuqitTrpGbOBcvf0zGTOhZPF0_xzalk7HTLfK_QymsZa6yEp-2t0K-bH-IanTzh9BpGQ"
    cliente_autenticacion = MSGraphAuth(
        '952ce091-2362-481e-aa37-61325d6f2e0f',
        'jjk8Q~9~wfmhW4b-N2FDX1dY7mT1_gvgH0Kivc7y',
        'a177ae79-1984-4633-97c2-db990f28feef',
        '1.ATQAea53oYQZM0aXwtuZDyj-75HgLJViIx5IqjdhMl1vLg9QAXk0AA.AgABAwEAAABVrSpeuWamRam2jAF1XRQEAwDs_wUA9P-3Mfa8Npd6DC4jHN4gvXXWHnPxsrNKugj5GptAQtbFxDKyraMKEx6nutv8BPTGY5gCo2VSyTUVzIhfyEIL2xSa7w04SmU22iURKbLK0BZpLbBAmE5dPu-75614vPMcoH8k0EpFh_xlKZE6UwE4e6KJRTqUVHfAI902XfvUonUkYlvDhpmbb04H2eCA99yiZaESK2ijruKcOZxOX8op0aebN_5yWwP_iT52FTHUOBpCQcF2X-Gd78EA3T89i-gbZqk5v49iFMx9tWADKrX54NQGVx6OHq82YGpxf-OtxawbrOmRQ9GR28BZZMlYSBrxd5dcqgb6lc-ZPw3DxAVZ-onuKFiLf_sZMBcMmU0rMxuS5BR2H1znKnXfEBwMplI1NiD7NU_VrZDSXuYzPYTAv1f-abd9WfWfCgxDiarC4msFjJSCDYpCkPGQbavoQJNLi8tRaAq0B-KxWk1fqKm-IfMKsubh4rEWRd8fT_-nMNPvWEgYStPWXOQQYNkkL5AHX4IvpJRMmbsqMUwpOgQLaGaXW3LGyEZ2sXGU3jeZxCV3qoTWDrG_njN_nKi7aZ-ZOWz68KhmRFxQ-kB9Tor9IgUFbIDj8f1rbh37-VBjTqXkbRGwt2iyBZhle2JFBYvwduWLiZSuKpaojhRblaJNnk3VmgA0xDdP06zteZpPYjzXbaSvcGgCMwq1qWCcISvBbdorLrceOhyqr7CScpyJQnYyXPrBs4i7BQScCjNyr7sK9tUFWT5MEYL2Q3A85k5Xvjl0VGPt-cBejH2PgF3NnvtbllzVutVs1PIdlzRjWE8E6YTTEPoSY_Or8b-3h0uj5crqmxnld1AuD8FZW9SXYLMLy8aoQlPPW1_IPMDxbofdrxpUTgVqopq_U_leLIUaXMbPFCw-OUnixxwyno00M6mYdxsnY2Lqi8BtzkDcrPwALT99y78U-oTqRhEzm4YlwNP1tbqRuGuIAg40I4AEHcIX5mB0oWVxqdCd0E5IsXa-svSMX4Hpg7akX0VSjVzGJC35dvY5TmMe7Y7ot9DhweVvMpcY_Y70XD31kPuIHUGKqcQVMbYLImspE6UUAIicr2fUx7lW2LO60D2fT8LjM5S5DHwnGuzVww'
    )
    token = cliente_autenticacion.renovar_access_token()
    cliente_api = MSGraphAPI(token=token)
    graph_api = MSGraphAPI(token)
    drives = graph_api.list_drives("kryptocolombia.sharepoint.com")
    drive_id = drives[3]["id"]
    #folders = graph_api.list_folders(hostname="kryptocolombia.sharepoint.com", drive_id=drive_id, parent_folder_path="Innovación y Tecnología/IntegrIA/Proyectos automatización/07 Medios Magnéticos/text")
    #print(folders)
    #folders = graph_api.list_folders(hostname="kryptocolombia.sharepoint.com", drive_id=drive_id,
    #                                 parent_folder_path="Innovación y Tecnología/IntegrIA/Proyectos automatización/07 Medios Magnéticos/text")

    #result=graph_api.delete_all_files_in_folder(hostname="kryptocolombia.sharepoint.com",
    #                                     drive_id=drive_id,
    #                                     folder_path="Innovación y Tecnología/IntegrIA/Proyectos automatización/07 Medios Magnéticos/text"
    #                                     )

    result = graph_api.download_file_from_sharepoint(hostname="kryptocolombia.sharepoint.com",
                                                     drive_id=drive_id,
                                                     folder_path="Innovación y Tecnología/IntegrIA/Proyectos automatización/07 Medios Magnéticos/text",
                                                     download_to="")
    print(result)


    #print(graph_api.upload_file_to_sharepoint(hostname="kryptocolombia.sharepoint.com",drive_id=drive_id,file_path="C:\\Users\\Krypto\\Downloads\\4f34bdcd-e560-471f-baae-0da3fdc8b8d3.pdf",folder_path="Innovación y tecnología/IntegrIA/Proyectos Automatización/07 Medios Magnéticos/insumos/insumos_aliaddo/SIMIAN S.A.S/balance_terceros"))









