# Laboratorio 3: Uso de BiTalino para EMG y ECG
Durante el laboratorio se realizó la adquisición de señales biomédicas utilizando el kit **BITalino (r)evolution** y el software **OpenSignals (r)evolution**. La sesión permitió familiarizarnos con la configuración del dispositivo, la conexión de los sensores y electrodos, la adquisición de señales y la posterior extracción de los datos registrados.

En particular, se trabajó con la adquisición de **electromiografía (EMG)**, registrando la actividad eléctrica muscular mediante electrodos superficiales. Se observaron las diferencias entre los periodos de reposo y de activación muscular, identificando un incremento de la amplitud de la señal durante la contracción.

Finalmente, las adquisiciones realizadas en OpenSignals fueron almacenadas y posteriormente importadas a **Python**, permitiendo acceder a los datos crudos y representar nuevamente la señal fuera del software de adquisición.

## Objetivos específicos de la práctica
- Adquirir señales biomédicas de EMG y ECG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolution
---

A continuación se detalla el paso a paso seguido durante la sesión del laboratorio.
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

## Conexión del sensor EMG y colocación de electrodos
Una vez configurado el dispositivo en OpenSignals (r)evolution, se realizó la conexión del sensor de **electromiografía (EMG)** al BITalino. Se utilizó el cable correspondiente al sensor y se conectó al canal analógico **A1**, previamente habilitado en el software para la adquisición de la señal.

<div align="center">
 <img width="790" height="600" alt="image" src="https://github.com/user-attachments/assets/b7ace4ea-cebf-4dd2-b2dc-64fc3ef2833f" />

 **Figura 4.** Conexión del sensor EMG al canal analógico A1 del BITalino (r)evolution para la adquisición de la actividad eléctrica muscular.
</div>

Durante la práctica se registró la actividad electromiográfica de dos músculos: **bíceps y tríceps**. Para cada adquisición se colocaron electrodos superficiales en la región correspondiente al músculo de interés y se utilizó adicionalmente un **electrodo de referencia** colocado en el codo.

<div align="center">
 <img width="400" height="600" alt="image" src="https://github.com/user-attachments/assets/2e147336-04e9-4b63-96dd-3f05dde2da46" />

 **Figura 5.** Colocación de los electrodos superficiales para la adquisición de la señal EMG del bíceps

 <img width="400" height="600" alt="image" src="https://github.com/user-attachments/assets/73bc4d06-18be-4156-bfec-7103bef622fb" />

 **Figura 6.** Colocación de los electrodos superficiales para la adquisición de la señal EMG del tríceps

</div>

## Adquisición de las señales EMG
Una vez realizada la conexión del sensor y la colocación de los electrodos, se inició la adquisición de las señales EMG mediante **OpenSignals (r)evolution**. El protocolo se aplicó tanto para el **bíceps** como para el **tríceps**, con el objetivo de observar los cambios en la actividad electromiográfica bajo diferentes niveles de activación muscular.

Para cada músculo se evaluaron tres condiciones:

1. **Reposo:** el participante mantuvo el músculo relajado, evitando realizar movimientos voluntarios durante el registro.
2. **Movimiento leve:** se realizó el movimiento correspondiente a la activación del músculo sin aplicar una resistencia externa adicional.
3. **Movimiento con fuerza en dirección contraria:** se realizó el movimiento mientras se aplicaba una fuerza externa en sentido contrario, generando una mayor resistencia al movimiento y, por tanto, una mayor demanda de activación muscular.

Para cada una de las condiciones se realizaron **tres adquisiciones independientes**. Entre adquisiciones se mantuvo un periodo de descanso de aproximadamente **30 segundos a 1 minuto**, con la finalidad de permitir la recuperación antes de realizar la siguiente toma.


<div align="center">
 
https://github.com/user-attachments/assets/7c319073-d8d7-4ad9-9d49-2b0679783f39
 
**Video 1.** Ejecución del movimiento leve durante la adquisición de la señal EMG del bíceps.

</div>

Durante cada adquisición, la señal EMG fue visualizada en tiempo real mediante OpenSignals. Esto permitió observar las variaciones de amplitud de la señal entre los periodos de reposo y las condiciones de activación muscular.

<div align="center">

https://github.com/user-attachments/assets/bdf2c63a-f7f7-4205-9f6c-91244807fbeb
 
**Video 2.** Visualización en OpenSignals (r)evolution de la señal EMG durante la adquisición correspondiente al movimiento leve del bíceps.
</div>

## Guardado y extracción de datos
Una vez finalizada cada adquisición, OpenSignals (r)evolution permitió guardar los registros obtenidos durante la práctica. Las señales fueron almacenadas en formato **`.h5`**, correspondiente a archivos HDF5 que organizan los datos de adquisición de manera estructurada. Cada archivo contiene la información asociada al dispositivo BITalino, los canales registrados y las muestras adquiridas durante la medición.

<div align="center">
 
<img width="2992" height="1894" alt="image" src="https://github.com/user-attachments/assets/306bcf76-21cc-41f0-861e-d03eb37d128f" />

**Figura 7.** Archivos de adquisición generados por OpenSignals (r)evolution en formato `.h5`.

</div>

## Lectura de los archivos `.h5` en Python
Para visualizar las señales fuera de OpenSignals, los archivos `.h5` fueron leídos utilizando Python. Se empleó la librería `h5py` para acceder a la estructura interna del archivo y extraer el canal correspondiente a la señal EMG.

Los archivos `.h5` generados por OpenSignals fueron trasladados a la carpeta correspondiente al **Laboratorio 3 dentro del repositorio de GitHub**, con el fin de mantener los datos adquiridos junto con los archivos utilizados para su procesamiento.

Posteriormente, se abrió el repositorio en **Visual Studio Code (VS Code)** y se creó un archivo `.py` para realizar la lectura y visualización de las señales. En el código se utilizaron las librerías `h5py` para acceder al archivo HDF5, `NumPy` para manejar las muestras y `Matplotlib` para realizar el ploteo de la señal EMG.

<div align="center">
 
<img width="3000" height="1886" alt="image" src="https://github.com/user-attachments/assets/cb69f77c-d7b6-4855-b8c1-7e8df50be1d9" />

**Figura 8.** Incorporación de archivos `.h5` al repositorio y desarrollo del código python en Visual Studio.

</div>


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

A continuación, se presenta una de las adquisiciones correspondientes al **bíceps durante la condición de movimiento leve**. La señal mostrada corresponde a los datos crudos extraídos directamente del archivo `.h5`, sin aplicar etapas adicionales de filtrado o procesamiento.

<div align="center">
 
<img width="1400" height="500" alt="bicep_normal" src="https://github.com/user-attachments/assets/be23bffd-919a-4a1a-96ba-03af8e51bbf2" />


**Figura 9.** Señal EMG cruda del bíceps durante la condición de movimiento leve, extraída del archivo `.h5` y graficada mediante Python. El eje horizontal representa el tiempo en segundos y el eje vertical los valores registrados por el convertidor analógico-digital (ADC) del sistema de adquisición.

</div>

 Los demás registros EMG, junto con los archivos `.h5` correspondientes, pueden consultarse en la carpeta [`Data_OpenSignals`](./Data_OpenSignals/) del repositorio.
