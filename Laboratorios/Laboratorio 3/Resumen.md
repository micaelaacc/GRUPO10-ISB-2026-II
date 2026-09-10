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


https://github.com/user-attachments/assets/54f6385e-a78c-4480-bd20-6d8e519b9c57

**Video 3.** Ejecución del movimiento con fuerza en dirección contraria durante la adquisición de la señal EMG del tríceps.

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

La señal presentada en la Figura 9 corresponde al registro de **EMG crudo del bíceps durante un movimiento leve**. Al inicio de la adquisición, aproximadamente entre **0 y 3 s**, la señal presenta pequeñas variaciones alrededor de un nivel basal cercano a **510 ADC**, asociado a un periodo de baja actividad muscular. A partir de aproximadamente los **3–5 s**, se observa un incremento progresivo en la amplitud de las oscilaciones de la señal, correspondiente al inicio de la activación del bíceps durante el movimiento. La actividad electromiográfica aumenta hasta alcanzar su mayor amplitud aproximadamente entre los **17 y 21 s**, donde se observan las mayores variaciones respecto al nivel basal. Posteriormente, la amplitud disminuye progresivamente entre aproximadamente **21 y 29 s**, indicando una reducción de la activación muscular. Finalmente, desde aproximadamente los **30 s**, la señal retorna a valores cercanos al nivel basal, correspondientes nuevamente a una condición de baja actividad muscular. El aumento de la amplitud de la señal durante el movimiento refleja una mayor actividad eléctrica registrada en el músculo respecto a los periodos de reposo. Debido a que se presenta la **señal cruda**, todavía se conserva el nivel de offset alrededor del cual oscila el registro y no se han aplicado etapas de filtrado, rectificación o extracción de envolvente.

 Los demás registros EMG, junto con los archivos `.h5` correspondientes, pueden consultarse en la carpeta [`Data_OpenSignals`](./Data_OpenSignals/) del repositorio.

## Quizz
A continuación, se presentan y desarrollan las preguntas propuestas en la guía de laboratorio, relacionadas con los fundamentos de la adquisición y análisis de señales biomédicas mediante BITalino.

**Q1. ¿Cuáles son las frecuencias significativas para adquisiciones EMG? ¿Son las
mismas en todas las zonas del cuerpo, como el área facial?**

Las señales EMG de superficie contienen información útil principalmente en el rango de 20
a 500 Hz, concentrando la mayor parte de su energía entre 50 y 150 Hz. Este rango no es
exactamente igual en todas las zonas del cuerpo: en músculos grandes como el bíceps o el
tríceps, la energía se concentra en la parte más baja-media del espectro debido a fibras
musculares más lentas y de mayor tamaño. En cambio, en músculos faciales, al ser más
pequeños, superficiales y con fibras de contracción más rápida, la energía tiende a
desplazarse hacia frecuencias relativamente más altas dentro de ese mismo rango general.

**Q2. ¿Qué tipo de filtro es esencial al trabajar con señales EMG? ¿Por qué es
necesario aplicarlo?**

Es esencial aplicar un filtro pasa-banda (band-pass) de aproximadamente 20-500 Hz, junto
con un filtro notch en 50/60 Hz. El filtro pasa-banda elimina componentes de muy baja
frecuencia (artefactos de movimiento, deriva de línea base) y de muy alta frecuencia (ruido
electrónico) que no corresponden a la actividad muscular real. El filtro notch es necesario
porque elimina la interferencia de la red eléctrica (50 Hz en la mayoría de países, 60 Hz en
otros), que se acopla fácilmente a los electrodos y contamina la señal. Sin estos filtros, la
señal EMG quedaría dominada por ruido y no reflejaría fielmente la actividad muscular.

**Q3. ¿Cómo difiere la amplitud en cada contracción muscular? ¿Hay diferencia según
la ubicación corporal?**

En mis registros de bíceps y tríceps se observa que la amplitud de la señal EMG aumenta
progresivamente conforme se incrementa la fuerza de contracción: al inicio los valores
oscilan cerca de la línea base (~500-520 ADC), y a medida que la contracción se hace más
intensa, los picos aumentan considerablemente (hasta 700 en bíceps y cerca de 1000 en
tríceps). Esto se debe al reclutamiento de más unidades motoras y al aumento de su
frecuencia de disparo conforme se requiere más fuerza.

En cuanto a la ubicación corporal, sí existen diferencias: músculos grandes y superficiales
como bíceps y tríceps generan amplitudes más altas debido a su mayor masa muscular
activa bajo el electrodo, mientras que músculos más pequeños o profundos (como los
faciales) suelen presentar amplitudes menores.

**Q4. Screenshot de EMG de un músculo trabajado (Sección D)**

<div align="center">
 
<img width="1400" height="500" alt="bicep_normal" src="https://github.com/user-attachments/assets/be23bffd-919a-4a1a-96ba-03af8e51bbf2" />
 
</div>

En esta captura se observa la señal EMG del bíceps durante una contracción voluntaria. La
señal permanece estable alrededor de la línea base (~510 ADC) durante los primeros
segundos, correspondientes al estado de reposo del músculo. Aproximadamente entre los
segundos 10 y 25 se observa un incremento notable en la amplitud de la señal, con picos
que llegan hasta ~610 ADC, lo cual corresponde al momento en que se realizó la
contracción muscular (flexión del brazo/codo activando el bíceps). Después del segundo 30,
la señal vuelve a estabilizarse cerca de la línea base, indicando el retorno del músculo al
reposo.
Esta señal corresponde a lo esperado: en reposo, un músculo relajado genera una actividad
eléctrica mínima (ruido de fondo), mientras que al contraerse voluntariamente se activa un
mayor número de unidades motoras, lo que se traduce en un aumento claro y temporal de
la amplitud de la señal, seguido de un retorno a la línea base al finalizar la contracción. La
acción realizada fue una flexión del antebrazo (curl de bíceps) para activar deliberadamente
el músculo bíceps braquial.

**Q5. ¿La amplitud EMG equivale a la cantidad de fuerza generada por el músculo?**

No, la amplitud EMG no es equivalente a la fuerza generada, aunque sí guarda una relación
con ella. Esta relación es generalmente no lineal y está influenciada por factores como la
ubicación del electrodo, el grosor de tejido adiposo entre el músculo y el electrodo, el
crosstalk de músculos adyacentes, y el nivel de fatiga muscular. Por esta razón, la amplitud
EMG debe interpretarse como un indicador indirecto de la actividad muscular y no como una
medida exacta de la fuerza producida.

 ## Conclusiones
 - Se logró realizar la **adquisición de señales electromiográficas (EMG) mediante el sistema BITalino (r)evolution**, configurando correctamente el canal A1 para EMG y utilizando una frecuencia de muestreo de **1000 Hz**.

- Se registró la actividad muscular del **bíceps y tríceps** bajo tres condiciones: reposo, movimiento leve y movimiento con resistencia. La visualización de las señales permitió reconocer variaciones en la amplitud del EMG asociadas con los diferentes periodos de actividad muscular.

- OpenSignals (r)evolution permitió realizar la **adquisición, visualización y almacenamiento de las señales**, generando archivos en formato `.h5` que posteriormente pudieron ser incorporados al repositorio para su análisis.

- Mediante Python y la librería `h5py` fue posible acceder a la estructura de los archivos `.h5`, identificar el canal correspondiente al EMG y extraer sus muestras. Asimismo, utilizando `NumPy` y `Matplotlib` se reconstruyó el eje temporal y se representó gráficamente la **señal EMG cruda**.

- La práctica permitió integrar las diferentes etapas de un proceso básico de adquisición de señales biomédicas: **colocación de electrodos, configuración del sistema de adquisición, registro de la señal, almacenamiento de los datos y posterior visualización mediante herramientas computacionales**.

