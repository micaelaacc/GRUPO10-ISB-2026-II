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
Primero, se activó el Bluetooth de la computadora y se buscó el dispositivo BITalino disponible como se muestra en la Figura 1. Una vez identificado, se realizó el emparejamiento desde la configuración de Windows para permitir posteriormente la comunicación con OpenSignals (r)evolution.

<div align="center">
<img width="2046" height="824" alt="image" src="https://github.com/user-attachments/assets/2cf34765-1510-42e5-9c46-224908df8c10" />

  **Figura 1.** Dispositivo BITalino emparejado mediante Bluetooth en Windows.
</div>

Luego se abrió el software **OpenSignals (r)evolution)** y se realizó la búsqueda de dispositivos disponibles. El programa detectó correctamente la tarjeta BITalino previamente emparejada.

<div align="center">
<img width="3000" height="1900" alt="bitalino found" src="https://github.com/user-attachments/assets/3676b60c-b22c-4fdb-ab3f-06c856c025cd" />

  **Figura 2.** Detección del dispositivo BITalino en OpenSignals.
</div>

Una vez habilitado el dispositivo, se configuró el canal analógico correspondiente al sensor de electromiografía. Se seleccionó el canal **A1** como señal **EMG** y se estableció una frecuencia de muestreo de **1000 Hz**, mientras que los demás canales analógicos permanecieron deshabilitados.

<div align="center">
<img width="1624" height="1360" alt="seleccionar canal" src="https://github.com/user-attachments/assets/299db446-e5cc-4d86-a1a9-66f04950727d" />

  **Figura 3.** Configuración del BITalino en OpenSignals.
</div>

