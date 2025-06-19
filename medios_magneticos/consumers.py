import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EstadoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # Simula enviar estado repetidamente (reemplaza por lógica real)
        await self.send_estado_periodicamente()

    async def disconnect(self, close_code):
        pass

    async def send_estado_periodicamente(self):
        import asyncio
        while True:
            estado_data = {
                "robot": "subir_insumos.robot",
                "estado": "finalizado",  # Este dato vendrá de la lógica real
                "detalle": "Proceso terminado correctamente"
            }
            await self.send(text_data=json.dumps(estado_data))
            await asyncio.sleep(5)  # Simula espera de actualización