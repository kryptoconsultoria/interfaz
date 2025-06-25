import msal
from urllib.parse import urlparse, parse_qs
from django.conf import settings

class MSGraphAuth:
    def __init__(self, client_id, client_secret, tenant_id, refresh_token=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authority = f"https://login.microsoftonline.com/{tenant_id}"
        self.scopes = ["https://graph.microsoft.com/.default"]
        self.refresh_token = refresh_token
        self.app = msal.ConfidentialClientApplication(
            client_id=settings.ID_CLIENTE,
            client_credential=settings.CLIENT_SECRET,
            authority=settings.AUTHORITY
        )

    def obtener_access_token(self):
        """
        Flujo de autorización:
         1) Inicia el auth code flow (te da una URL).
         2) Abres la URL, autorizas y Azure te redirige.
         3) Copias la URL de redirección completa aquí.
         4) MSAL extrae el 'code' y obtiene tu token.
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


if __name__ == "__main__":
    auth_client = MSGraphAuth(
        "952ce091-2362-481e-aa37-61325d6f2e0f",
        "jjk8Q~9~wfmhW4b-N2FDX1dY7mT1_gvgH0Kivc7y",
        "a177ae79-1984-4633-97c2-db990f28feef",
        f'''1.ATQAea53oYQZM0aXwtuZDyj-75HgLJViIx5IqjdhMl1vLg9QAXk0AA.AgABAwEAAABVrSpeuWamRam2jAF1XRQEAwDs_wUA9P-3Mfa8Npd6DC4jHN4gvXXWHnPxsrNKugj5GptAQtbFxDKyraMKEx6nutv8BPTGY5gCo2VSyTUVzIhfyEIL2xSa7w04SmU22iURKbLK0BZpLbBAmE5dPu-75614vPMcoH8k0EpFh_xlKZE6UwE4e6KJRTqUVHfAI902XfvUonUkYlvDhpmbb04H2eCA99yiZaESK2ijruKcOZxO
    X8op0aebN_5yWwP_iT52FTHUOBpCQcF2X-Gd78EA3T89i-gbZqk5v49iFMx9tWADKrX54NQGVx6OHq82YGpxf-OtxawbrOmRQ9GR28BZZMlYSBrxd5dcqgb6lc-ZPw3DxAVZ-onuKFiLf_sZMBcMmU0rMxuS5BR2H1znKnXfEBwMplI1NiD7NU_VrZDSXuYzPYTAv1f-abd9WfWfCgxDiarC4msFjJSCDYpCkPGQbavoQJNLi8tRaAq0B-KxWk1fqKm-IfMKsubh4rEWRd8fT_-nMNPvWEgYStPWXOQQYNkkL5AHX
    4IvpJRMmbsqMUwpOgQLaGaXW3LGyEZ2sXGU3jeZxCV3qoTWDrG_njN_nKi7aZ-ZOWz68KhmRFxQ-kB9Tor9IgUFbIDj8f1rbh37-VBjTqXkbRGwt2iyBZhle2JFBYvwduWLiZSuKpaojhRblaJNnk3VmgA0xDdP06zteZpPYjzXbaSvcGgCMwq1qWCcISvBbdorLrceOhyqr7CScpyJQnYyXPrBs4i7BQScCjNyr7sK9tUFWT5MEYL2Q3A85k5Xvjl0VGPt-cBejH2PgF3NnvtbllzVutVs1PIdlzRjWE8E6YTTEPoSY_Or8b-3h0uj5crqmxnld1AuD8FZW9SXYLMLy8aoQlPPW1_IPMDxbofdrxpUTgVqopq_U_leLIUaXMbPFCw-OUnixxwyno00M6mYdxsnY2Lqi8BtzkDcrPwALT99y78U-oTqRhEzm4YlwNP1tbqRuGuIAg40I4AEHcIX5mB0oWVxqdCd0E5IsXa-svSMX4Hpg7akX0VSjVzGJC35dvY5TmMe7Y7ot9DhweVvMpcY_Y70XD31kPuIHUGKqcQVMbYLImspE6UUAIicr2fUx7lW2LO60D2fT8LjM5S5DHwnGuzVww'''
    )
    try:
        #token_data = auth_client.obtener_access_token()
        #access_token = token_data["access_token"]

        # Ejemplo de cómo renovar el token más adelante
        renovado = auth_client.renovar_access_token()
        print(f"\nToken renovado:\n{renovado}")
    except Exception as e:
        print(f"\nHa ocurrido un error: {e}")
