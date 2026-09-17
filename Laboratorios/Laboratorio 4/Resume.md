# Laboratorio 4: Adquisición de ECG con BITalino y OpenSignals
La sesión nos permitió evaluar las distintas derivaciones de ECG.En particular, se trabajó con la adquisición de electrocardiografía (ECG), registrando la actividad eléctrica cardíaca mediante electrodos superficiales bajo distintas configuraciones de las derivaciones de Einthoven. Se observaron las variaciones en la señal y en los complejos bajo diferentes condiciones fisiológicas y de actividad física (como reposo, hiperventilación, hipoventilación y post-esfuerzo).

Finalmente, las adquisiciones realizadas en OpenSignals fueron almacenadas y posteriormente importadas a Python, permitiendo acceder a los datos crudos y representar nuevamente la señal fuera del software de adquisición.

## Objetivos específicos de la práctica
- Adquirir señales biomédicas de ECG mediante configuraciones de electrodos superficiales.
- Hacer una configuración correcta del kit BiTalino y OpenSignals para la lectura cardíaca.
- Evaluar el comportamiento de la señal de ECG ante diferentes estados fisiológicos y de esfuerzo físico.
- Extraer y procesar la información de las señales de ECG en Python para su análisis detallado.
---

## Configuración de BITalino y OpenSignals
Antes de iniciar la adquisición, se verificó que el kit BITalino (r)evolution contara con los componentes necesarios para la práctica. Se conectó la batería a la placa y posteriormente se encendió el dispositivo, dejándolo disponible para establecer la comunicación inalámbrica con la computadora.

Con el BITalino encendido, se activó el Bluetooth de la computadora y se buscó el dispositivo BITalino disponible como se muestra en la Figura 1. Una vez identificado, se realizó el emparejamiento desde la configuración de Windows para permitir posteriormente la comunicación con OpenSignals (r)evolution.

<div align="center">
<img width="2046" height="824" alt="image" src="https://github.com/user-attachments/assets/2cf34765-1510-42e5-9c46-224908df8c10" />

  **Figura 1.** Dispositivo BITalino emparejado mediante Bluetooth en Windows.
</div>

Luego se abrió el software **OpenSignals (r)evolution)** y se realizó la búsqueda de dispositivos disponibles. El programa detectó correctamente la tarjeta BITalino previamente emparejada tal como se muestra en la Figura 2.

<div align="center">
<img width="3000" height="1900" alt="bitalino found" src="https://github.com/user-attachments/assets/3676b60c-b22c-4fdb-ab3f-06c856c025cd" />

  **Figura 2.** Detección del dispositivo BITalino en OpenSignals.
</div>

Una vez habilitado el dispositivo, se configuró el canal analógico correspondiente al sensor de electromiografía. Se seleccionó el canal **A1** como señal **EMG** y se estableció una frecuencia de muestreo de **1000 Hz**, mientras que los demás canales analógicos permanecieron deshabilitados como se muestra en la Figura 3.

<div align="center">
<img width="1624" height="1360" alt="seleccionar canal" src="https://github.com/user-attachments/assets/299db446-e5cc-4d86-a1a9-66f04950727d" />

  **Figura 3.** Configuración del BITalino en OpenSignals.
</div>
## Conexión del sensor ECG y colocación de electrodos
Una vez configurado el dispositivo en OpenSignals (r)evolution, se realizó la conexión del sensor de **electrocardiograma (EMG)** al BITalino. Se utilizó el cable correspondiente al sensor y se conectó al canal analógico **A1**, previamente habilitado en el software para la adquisición de la señal.
<div align="center">
 <img width="790" height="600" alt="image" src="https://github.com/user-attachments/assets/b7ace4ea-cebf-4dd2-b2dc-64fc3ef2833f" />

 **Figura 4.** Conexión del sensor de ECG al canal analógico A1 del BITalino (r)evolution para la adquisición de la actividad eléctrica cardíaca.
</div>
Durante la práctica se registró la actividad eléctrica cardíaca utilizando las derivaciones de Einthoven. Para la adquisición se colocaron electrodos superficiales en las regiones correspondientes a los puntos clave de las derivaciones —específicamente debajo de las clavículas y en la zona cercana al abdomen/ombligo—, y se se iban rotando y reposicionando dependiendo de la derivación específica que se evaluaba.

# Faltan la imagen (nose como se pone :c)

<div align="center">
 
  **Figura 5.** Colocación de los electrodos superficiales para la adquisición de la señal ECG
</div>

## Adquisición de la señal de ECG

Una vez realizada la conexión del sensor y la colocación de los electrodos, se inició la adquisición de las señales de electrocardiografía (ECG) mediante OpenSignals (r)evolution. El protocolo experimental abarcó la evaluación bajo diferentes condiciones fisiológicas y de actividad física para observar las variaciones en la señal cardíaca y en los intervalos temporales.

Para cada una de las configuraciones de derivación evaluadas —cubriendo las distintas posiciones y rotaciones de los electrodos según las derivaciones de Einthoven— se llevaron a cabo las siguientes etapas experimentales:

1. **Reposo inicial:** Se realizó un registro de la señal base con el participante en estado de reposo, manteniendo una respiración normal y evitando movimientos voluntarios durante aproximadamente 30 segundos, con el fin de establecer una línea base libre de artefactos. Esto se repitió para las diferentes derivaciones de Einthoven evaluadas.
2. **Hiperventilación:** Se ejecutó un ciclo de respiración profunda y acelerada estructurado en tres ciclos consecutivos, manteniendo periodos de descanso o reposo de aproximadamente 1 minuto entre cada uno para evaluar el comportamiento del ritmo cardíaco ante los cambios ventilatorios.
3. **Hipoventilación:** Se solicitó al participante realizar una retención de la respiración controlada, manteniendo un periodo de reposo previo y posterior de aproximadamente 1 minuto a 1 minuto y medio para permitir la estabilización del sistema cardiovascular en las distintas derivaciones.
4. **Actividad física (Post-esfuerzo):** Se realizó una prueba de esfuerzo físico (con una duración aproximada de 5 a 10 minutos o hasta que el participante se encontrara físicamente agitado). Inmediatamente al finalizar, se procedió a ajustar los electrodos con la mayor rapidez posible para capturar el registro exacto en todas las derivaciones (esta fase de alta intensidad se realizó en una única intervención).

Durante cada etapa, la señal de ECG fue supervisada en tiempo real para asegurar una correcta amplitud del complejo QRS y minimizar el ruido antes de almacenar los datos para su posterior análisis en Python.

# Faltan los videos (nose como se pone :c)

 **Video 1.** Ejecución de la prueba de ECG en reposo y Adquisición de la señal de ECG  

 **Video 2.** Ejecución de los ciclos de hiperventilación

 **Video 3.** Ejecución de la actividad física (Post-esfuerzo)

## Guardado y extracción de datos
Una vez finalizada cada adquisición, OpenSignals (r)evolution permitió guardar los registros obtenidos durante la práctica. Las señales fueron almacenadas en formato **`.h5`**, correspondiente a archivos HDF5 que organizan los datos de adquisición de manera estructurada. Cada archivo contiene la información asociada al dispositivo BITalino, los canales registrados y las muestras adquiridas durante la medición.

** Faltan los videos (nose como se pone :c)**

**Figura 6.** Archivos de adquisición generados por OpenSignals (r)evolution en formato `.h5`.


## Lectura de los archivos `.h5` en Python
Para visualizar las señales fuera de OpenSignals, los archivos `.h5` fueron leídos utilizando Python. Se empleó la librería `h5py` para acceder a la estructura interna del archivo y extraer el canal correspondiente a la señal ECG.

Los archivos `.h5` generados por OpenSignals fueron trasladados a la carpeta correspondiente al **Laboratorio 4 dentro del repositorio de GitHub**, con el fin de mantener los datos adquiridos junto con los archivos utilizados para su procesamiento.

Posteriormente, se abrió el repositorio en **Visual Studio Code (VS Code)** y se creó un archivo `.py` para realizar la lectura y visualización de las señales. En el código se utilizaron las librerías `h5py` para acceder al archivo HDF5, `NumPy` para manejar las muestras y `Matplotlib` para realizar el ploteo de la señal ECG.

** Faltan los videos (nose como se pone :c)**

**Figura 7.** Incorporación de archivos `.h5` al repositorio y desarrollo del código python en Visual Studio.

El siguiente código muestra la estructura utilizada para cargar uno de los archivos `.h5`, extraer las muestras correspondientes al canal EMG, construir el eje temporal a partir de la frecuencia de muestreo y finalmente representar la señal adquirida.

```python

from pathlib import Path
import h5py
import numpy as np
import matplotlib.pyplot as plt

# Ubicación del archivo
carpeta = Path(__file__).parent
archivo_h5 = carpeta / "mov_bicep.h5"

# Abrir archivo H5
with h5py.File(archivo_h5, "r") as f:

    dispositivo = "98:D3:51:FE:6E:5C"
    ruta_emg = f"{dispositivo}/raw/channel_1"

    # Extraer señal
    emg = np.array(f[ruta_emg]).flatten()

# Frecuencia de muestreo utilizada
fs = 1000  # Hz

# Crear eje temporal
tiempo = np.arange(len(emg)) / fs

# Graficar señal
plt.figure(figsize=(14, 5))
plt.plot(tiempo, emg)

plt.xlabel("Tiempo (s)")
plt.ylabel("Valor ADC")
plt.title("Señal EMG cruda")

plt.grid(True)
plt.tight_layout()
plt.show()

```
El mismo procedimiento fue utilizado para visualizar las diferentes adquisiciones realizadas, modificando el archivo `.h5` correspondiente a cada condición experimental.

## Conclusiones
