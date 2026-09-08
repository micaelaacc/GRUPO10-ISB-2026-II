from pathlib import Path
import h5py
import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# 1. UBICACIÓN DEL ARCHIVO
# ==========================================================

carpeta = Path(__file__).parent

archivo_h5 = carpeta / "mov_tricep1.h5"


# ==========================================================
# 2. ABRIR EL ARCHIVO H5
# ==========================================================

with h5py.File(archivo_h5, "r") as f:

    # Grupo correspondiente al BITalino
    dispositivo = "98:D3:51:FE:6E:5C"

    # Dataset que contiene el EMG crudo
    ruta_emg = f"{dispositivo}/raw/channel_1"

    # Extraer datos
    emg = np.array(f[ruta_emg]).flatten()


# ==========================================================
# 3. INFORMACIÓN DE LA SEÑAL
# ==========================================================

print("Número de muestras:", len(emg))
print("Valor mínimo:", np.min(emg))
print("Valor máximo:", np.max(emg))
print("Valor medio:", np.mean(emg))
print("Desviación estándar:", np.std(emg))


# ==========================================================
# 4. FRECUENCIA DE MUESTREO
# ==========================================================

# IMPORTANTE:
# Coloca aquí la frecuencia que configuraste en OpenSignals.
fs = 1000  # Hz


# ==========================================================
# 5. CREAR EJE DE TIEMPO
# ==========================================================

tiempo = np.arange(len(emg)) / fs

print("Duración:", len(emg) / fs, "segundos")


# ==========================================================
# 6. GRAFICAR EMG
# ==========================================================

plt.figure(figsize=(14, 5))

plt.plot(tiempo, emg, linewidth=0.8)

plt.xlabel("Tiempo (s)")
plt.ylabel("Valor ADC")
plt.title("Señal EMG - Tríceps")

plt.grid(True)

plt.tight_layout()

plt.show()