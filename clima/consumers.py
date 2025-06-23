import json
from asyncio import sleep
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class SensorDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.keep_sending = True

        while self.keep_sending:
            latest = await self.get_latest_measurement()
            if latest:
                await self.send(text_data=json.dumps({
                    'temperatura': latest.temperature_c,
                    'humedad': latest.humidity_percent,
                    'ppm': latest.air_quality_ppm,
                    'calidad': latest.air_quality_label
                }))
            await sleep(1)

    async def disconnect(self, close_code):
        self.keep_sending = False

    async def receive(self, text_data):
        pass

    @database_sync_to_async
    def get_latest_measurement(self):
        from .models import Measurement  # <- Importación movida aquí
        try:
            return Measurement.objects.latest('measured_at')
        except Measurement.DoesNotExist:
            return None
