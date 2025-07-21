import msal
from urllib.parse import urlparse, parse_qs

class MSGraphAuth:
    def __init__(self, client_id, client_secret, tenant_id, refresh_token=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authority = f"https://login.microsoftonline.com/{tenant_id}"
        self.scopes = ["https://graph.microsoft.com/.default"]
        self.refresh_token = refresh_token
        self.app = msal.ConfidentialClientApplication(
            client_id=self.client_id,
            client_credential=self.client_secret,
            authority=self.authority
        )

    def obtener_access_token(self):
        """
        Flujo de autorización:
         1) Inicia el auth code flow (te da una URL).
         2) Abre la URL, autorizas y Azure te redirige.
         3) Copia la URL de redirección complete aquí.
         4) MSAL extrae el 'code' y obtiene el token.
        """
        # (opcional) ver cuentas cacheadas
        print("Cuentas en cache:", self.app.get_accounts())

        # 1) inicio del flujo
        flow = self.app.initiate_auth_code_flow(
            scopes=self.scopes,
            redirect_uri="https://login.microsoftonline.com/common/oauth2/nativeclient"
        )
        print("Ve a esta URL e inicia sesión:\n", flow["auth_uri"])

        # 2+3) pide al usuario pegar la URL de redirección
        redirect_response = input("\nPega aquí la URL completa de redirección: ").strip()
        # 4) parsear los parámetros query (incluye 'code')
        qs = urlparse(redirect_response).query
        params = {k: v[0] for k, v in parse_qs(qs).items()}

        # 5) intercambio código por token
        result = self.app.acquire_token_by_auth_code_flow(flow, params)

        access_token = result.get("access_token")
        refresh_token = result.get("refresh_token")
        if access_token and refresh_token:
            return {"access_token": access_token, "refresh_token": refresh_token}
        else:
            error = result.get("error", "desconocido")
            description = result.get("error_description", "")
            raise Exception(f"Error al obtener el token: {error} - {description}")

    def renovar_access_token(self):
        """
        Renueva el access_token utilizando el refresh_token.
        """
        result = self.app.acquire_token_by_refresh_token(self.refresh_token, scopes=self.scopes)
        access_token = result.get("access_token")
        if access_token:
            return access_token
        else:
            error = result.get("error", "desconocido")
            description = result.get("error_description", "")
            raise Exception(f"Error al renovar el token: {error} - {description}")