import os
import django
import time
import serial

# Configurar entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estacion.settings')
django.setup()

from clima.models import Sensor, Measurement
from django.contrib.auth.models import User

# Conectar con Arduino
arduino = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)  # Esperar a que inicie el Arduino

# Buscar o crear sensor asociado al primer usuario
user = User.objects.first()  # Asegúrate de que exista al menos un usuario creado
sensor, created = Sensor.objects.get_or_create(
    name="Sensor Arduino Uno",
    defaults={
        'user': user,
        'location': 'Interior'
    }
)

print("Escuchando datos...")
while True:
    try:
        line = arduino.readline().decode('utf-8').strip()
        if line:
            partes = line.split('.')
            if len(partes) == 4:
                temperatura = float(partes[0].replace(',', '.'))
                humedad = float(partes[1].replace(',', '.'))
                ppm = float(partes[2].replace(',', '.'))
                calidad = partes[3].split(',')[-1].strip()  # <- Aquí está el cambio

                Measurement.objects.create(
                    sensor=sensor,
                    temperature_c=temperatura,
                    humidity_percent=humedad,
                    air_quality_ppm=ppm,
                    air_quality_label=calidad
                )

                print(f"Guardado: T={temperatura}°C, H={humedad}%, Calidad={calidad}, PPM={ppm}")
    except KeyboardInterrupt:
        print("\nLectura detenida.")
        break
    except Exception as e:
        print(f"Error: {e}")
